# Orchestrator Agent Specification

## Role
Central coordinator responsible for managing the entire content creation workflow, agent communication, and daily execution.

## Core Responsibilities
- Initialize daily workflow at scheduled times
- Coordinate inter-agent communication
- Monitor agent task completion
- Compile final deliverables
- Handle error recovery and fallbacks

## Skills Required
- **Workflow Management**: Execute complex multi-step processes
- **Agent Coordination**: Route tasks and information between agents
- **Time Management**: Ensure timely completion of all tasks
- **Quality Control**: Validate outputs before delivery
- **Error Handling**: Manage failures gracefully

## Tools & Integrations
- **Scheduling System**: Cron or similar for daily activation
- **Message Queue**: For agent communication (e.g., RabbitMQ)
- **State Management**: Track workflow progress
- **Notification System**: Slack/Email for status updates
- **Logging System**: Comprehensive activity logs

## Input Requirements
- Schedule configuration
- Agent registry and capabilities
- Workflow templates
- Error handling rules

## Output Format
```json
{
  "execution_date": "2024-01-15",
  "workflow_status": "completed",
  "agents_activated": 8,
  "tasks_completed": 24,
  "deliverables": {
    "content_ideas": 10,
    "linkedin_posts": 5,
    "viral_content": 3,
    "repurposing_suggestions": 15
  },
  "errors": [],
  "execution_time": "32 minutes"
}
```

## Activation Commands
```bash
# Manual activation
python orchestrator.py --activate --mode=full

# Scheduled activation (crontab)
0 9 * * * /usr/bin/python /path/to/orchestrator.py --activate --mode=daily

# Test mode
python orchestrator.py --test --agents=all
```

## Communication Protocol
- Uses JSON-RPC for agent communication
- Implements timeout and retry logic
- Maintains audit trail of all interactions

## Tone Guidelines
Adhere to the shared tone of voice defined in ../agents/tone-of-voice.md: authoritative, innovative, collaborative, value-oriented. Ensure all orchestrations, communications, and outputs reflect this tone, providing clear, professional, and insightful coordination that aligns with Oracle AI CoE standards.
