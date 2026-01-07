# AI CoE Use Case Agentic Department

## Overview
This department provides a streamlined, agentic workflow for transforming raw use cases into multi-asset content campaigns. The process is designed to be intelligent yet simple: a linear sequence of specialized agents that handle analysis, strategy, and content generation without unnecessary complexity.

## Workflow Philosophy
- **Sophisticated Intelligence**: Each agent leverages domain expertise and AI capabilities for deep insights
- **Simplicity in Execution**: Clear handoffs, standardized inputs/outputs, minimal tooling overhead
- **Reusability**: Templates and agents work across all use cases (Genetics, Finance, Retail, etc.)
- **Measurable Quality**: Built-in validation and optimization steps

## Core Agents
1. **Use Case Analyzer**: Extracts key elements, identifies Oracle hooks, quantifies value
2. **Audience Strategist**: Maps target audiences, tailors messaging, defines KPIs
3. **Content Generator**: Produces platform-specific assets (Slack, LinkedIn, etc.)
4. **Platform Adapter**: Optimizes for engagement metrics, SEO, and distribution

## Execution Flow
```xml
<workflow>
  <input>Raw use case document</input>
  <step id="1">
    <agent>use-case-analyzer</agent>
    <output>Structured use case analysis</output>
  </step>
  <step id="2">
    <agent>audience-strategist</agent>
    <output>Audience-specific content strategy</output>
  </step>
  <step id="3">
    <agent>content-generator</agent>
    <output>Draft content assets</output>
  </step>
  <step id="3.5">
    <agent>claims-validation</agent>
    <output>Validated content with claims registry and risk report</output>
    <gate>Publish gate must pass for step 4</gate>
  </step>
  <step id="4">
    <agent>platform-adapter</agent>
    <output>Optimized final assets</output>
  </step>
  <output>Multi-asset content package</output>
</workflow>
```

## File Structure
- `README.md`: This overview
- `agents/`: Individual agent definitions
- `templates/`: Reusable content templates
- `outputs/`: Generated content per use case

## Usage
1. Place new use case in parent folder
2. Run agents sequentially via this workflow
3. Review and deploy generated assets

## Quality Assurance
- Each agent includes validation checklists
- Output formats are standardized for consistency
- Performance metrics tracked per asset type

## Relationship to Existing Writing Process
The existing `writing_process/` agents (maestro, research, outlining, writing, editing, seo) are excellent for general content creation workflows. This Use Case Agentic Department is specialized for transforming technical use cases into multi-platform content campaigns, with domain-specific intelligence for Oracle solutions and audience segmentation. Use the appropriate process based on content type.
