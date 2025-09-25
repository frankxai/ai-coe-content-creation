# Daily Content Creation Workflow

## Activation Methods

### 1. Manual Activation
```bash
# Run the entire content creation pipeline
python activate_content_team.py --mode=full

# Run specific agents only
python activate_content_team.py --agents=ideation,writer

# Test mode (no actual posting)
python activate_content_team.py --mode=test
```

### 2. Scheduled Activation (Cron)
```bash
# Add to crontab for daily 9 AM execution
0 9 * * * /usr/bin/python3 /path/to/activate_content_team.py --mode=daily >> /path/to/logs/content_team.log 2>&1

# Multiple runs per day
0 9 * * * /usr/bin/python3 /path/to/activate_content_team.py --mode=morning
0 14 * * * /usr/bin/python3 /path/to/activate_content_team.py --mode=afternoon
```

### 3. Webhook Activation
```python
# Flask endpoint for webhook activation
@app.route('/activate-content-team', methods=['POST'])
def activate_team():
    auth_token = request.headers.get('Authorization')
    if validate_token(auth_token):
        mode = request.json.get('mode', 'full')
        result = content_team.activate(mode=mode)
        return jsonify(result)
```

## Daily Execution Timeline

### Phase 1: Ultimate Research & Ideation (9:00-9:30 AM)
```yaml
- Orchestrator: Initialize with inspirational focus from updated overall-strategy.md.
- Trend Researcher: Identify latest AI tooling trends.
- Content Ideation: Generate high-impact, inspirational ideas focused on tooling and transformations.
- Output: Consolidated research and ideas in 01-research-ideation.md
```

### Phase 2: Epic Content Creation & Adaptation (9:30-9:50 AM)
```yaml
- Content Creator: Craft ultimate, engaging content pieces.
- Platform Adapter: Optimize for all platforms in one go.
- Output: All adapted content in 02-content-output.md with embedded structures (JSON/YAML/XML).
```

### Phase 3: Validation & Final Report (9:50-10:00 AM)
```yaml
- Validator: Ensure world-class quality, inspirational tone.
- Orchestrator: Compile final report with metrics and next steps.
- Output: 03-final-report.md
```

## Configuration File
```yaml
# config/content_team_config.yaml
team_settings:
  activation_time: "09:00"
  timezone: "America/New_York"
  
  agents:
    orchestrator:
      timeout: 300
      retry_attempts: 3
    
    trend_researcher:
      sources:
        - twitter
        - linkedin
        - google_trends
      keywords:
        - "artificial intelligence"
        - "digital transformation"
        - "future of work"
    
    content_ideation:
      ideas_per_day: 10
      min_quality_score: 7.0
    
    linkedin_writer:
      posts_per_day: 5
      variations_per_post: 2
      
  guidelines:
    brand_voice: "../content-guidelines/brand-voice.md"
    world_class: "../content-guidelines/world-class-content.md"
    tone: "../agents/tone-of-voice.md"
    strategy: "../overall-strategy.md"
  
  delivery:
    channels:
      - email: "team@company.com"
      - slack: "#content-team"
      - dashboard: "https://dashboard.company.com/content"
    
    format: "html"
    include_analytics: true
```

## Ultimate Daily Report Template
```markdown
# Ultimate AI Inspiration Report - [DATE]

## Epic Highlights
- Revolutionary Trends Discovered: [Number]
- Transformational Content Created: [Number]
- Inspiration Score: [High Score]

## Inspirational Content Masterpieces
[Embedded full content with platform adaptations]

## Frontier Opportunities
[Latest tooling insights and ideas]

## Evolution Metrics
[Engagement predictions, improvements]

## Tomorrow's Horizon
[Inspirational focuses]

---
Powered by Ultimate Cline | [Timestamp]
```

## Error Handling
```python
error_protocols = {
    "agent_failure": {
        "action": "retry_with_backoff",
        "max_retries": 3,
        "fallback": "use_cached_data"
    },
    "api_limit": {
        "action": "queue_for_later",
        "notification": "alert_admin"
    },
    "no_trends_found": {
        "action": "use_evergreen_content",
        "source": "content_library"
    }
}
```

## Success Metrics
- Daily activation success rate: >95%
- Content generation time: <60 minutes
- Idea quality score: >7.0 average
- Engagement improvement: +20% month-over-month


## Step-by-Step Execution Instructions
To execute the workflow, follow these steps manually or automate via scripts. Use the prompt templates in prompts/ to interact with agents (e.g., via Grok4 or similar AI interface).

### Manual Execution:
1. **Activate Orchestrator**: Use prompts/orchestrator-prompt.md with current date and mode. Input: "{current_date}, {mode}, {previous_metrics}".
2. **Phase 1 - Data Gathering**:
   - Run Trend Researcher: Use prompts/trend-researcher-prompt.md with keywords, time_period, industry_focus.
   - Run Content Strategist: Use prompts/content-strategist-prompt.md with strategy_documents.
3. **Phase 2 - Ideation**:
   - Run Content Ideation: Use prompts/content-ideation-prompt.md with trends, strategy_themes, performance_insights.
4. **Phase 3 - Creation**:
   - Run LinkedIn Writer: Use prompts/linkedin-writer-prompt.md with content_idea, strategy_alignment, trends.
5. **Phase 4 - Adaptation**:
   - Run Platform Adapter: Use prompts/platform-adapter-prompt.md with original_content, platforms, guidelines.
6. **Phase 5 - Quality Check**: Manually or via Performance Analyst review outputs against world-class-content.md.
7. **Phase 6 - Compilation**: Compile results into the daily report template.

### Automated Execution:
- Update activation-script.py to chain these prompts using an AI API, passing outputs between agents.
- Test with --mode=test to simulate without posting.

This ensures seamless, high-value content production aligned with strategy.
