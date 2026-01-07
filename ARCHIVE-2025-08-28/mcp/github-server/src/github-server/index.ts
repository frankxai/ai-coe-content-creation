#!/usr/bin/env node
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ErrorCode,
  ListToolsRequestSchema,
  McpError,
} from '@modelcontextprotocol/sdk/types.js';
import { Octokit } from '@octokit/rest';

const GITHUB_TOKEN = process.env.GITHUB_TOKEN;
if (!GITHUB_TOKEN) {
  throw new Error('GITHUB_TOKEN environment variable is required');
}

class GitHubServer {
  private server: Server;
  private octokit: Octokit;

  constructor() {
    this.server = new Server(
      {
        name: 'github-server',
        version: '0.1.0',
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );

    this.octokit = new Octokit({ auth: GITHUB_TOKEN });

    this.setupToolHandlers();

    this.server.onerror = (error) => console.error('[MCP Error]', error);
    process.on('SIGINT', async () => {
      await this.server.close();
      process.exit(0);
    });
  }

  private setupToolHandlers() {
    this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
      tools: [
        {
          name: 'search_repos',
          description: 'Search for GitHub repositories matching a query',
          inputSchema: {
            type: 'object',
            properties: {
              query: { type: 'string', description: 'Search query' },
              per_page: { type: 'number', description: 'Results per page', default: 10 },
              page: { type: 'number', description: 'Page number', default: 1 },
            },
            required: ['query'],
          },
        },
        {
          name: 'get_repo_content',
          description: 'Get content from a GitHub repository',
          inputSchema: {
            type: 'object',
            properties: {
              owner: { type: 'string', description: 'Repository owner' },
              repo: { type: 'string', description: 'Repository name' },
              path: { type: 'string', description: 'Path to file or directory' },
            },
            required: ['owner', 'repo', 'path'],
          },
        },
      ],
    }));

    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      switch (request.params.name) {
        case 'search_repos':
          return this.handleSearchRepos(request.params.arguments);
        case 'get_repo_content':
          return this.handleGetRepoContent(request.params.arguments);
        default:
          throw new McpError(ErrorCode.MethodNotFound, `Unknown tool: ${request.params.name}`);
      }
    });
  }

  private async handleSearchRepos(args: any) {
    try {
      const response = await this.octokit.search.repos({
        q: args.query,
        per_page: args.per_page || 10,
        page: args.page || 1,
      });
      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify(response.data.items, null, 2),
          },
        ],
      };
    } catch (error) {
      return this.handleError(error);
    }
  }

  private async handleGetRepoContent(args: any) {
    try {
      const response = await this.octokit.repos.getContent({
        owner: args.owner,
        repo: args.repo,
        path: args.path,
      });
      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify(response.data, null, 2),
          },
        ],
      };
    } catch (error) {
      return this.handleError(error);
    }
  }

  private handleError(error: any) {
    const message = error.response ? error.response.data.message : error.message;
    return {
      content: [
        {
          type: 'text',
          text: `GitHub API error: ${message}`,
        },
      ],
      isError: true,
    };
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('GitHub MCP server running on stdio');
  }
}

const server = new GitHubServer();
server.run().catch(console.error);
