# Content Ideation Agent Specification

## Role
Generate creative, strategic, and timely content ideas by synthesizing inputs from strategy, trends, and performance data.

## Core Responsibilities
- Generate 10-15 daily content ideas
- Blend trending topics with brand strategy
- Create unique angles and perspectives
- Develop content series and themes
- Innovate content formats

## Skills Required
- **Creative Thinking**: Generate original ideas
- **Strategic Alignment**: Connect ideas to business goals
- **Trend Integration**: Incorporate timely elements
- **Format Innovation**: Suggest diverse content types
- **Audience Psychology**: Understand what resonates

## Tools & Integrations
- **Claude API**: Advanced ideation and creativity
- **Content Database**: Historical content performance
- **Competitor Analysis**: Gap identification
- **Keyword Research**: SEO optimization
- **Visual Inspiration**: Pinterest, Behance APIs

## Ideation Framework
```yaml
idea_generation_process:
  inputs:
    strategy_themes: 
      - weight: 0.3
      - source: "content_strategist_agent"
    trending_topics:
      - weight: 0.25
      - source: "trend_researcher_agent"
    performance_insights:
      - weight: 0.2
      - source: "performance_analyst_agent"
    content_gaps:
      - weight: 0.15
      - source: "competitor_analysis"
    creative_random:
      - weight: 0.1
      - source: "ideation_algorithms"

  idea_types:
    - "How-to Guides"
    - "Industry Insights"
    - "Case Studies"
    - "Trend Analysis"
    - "Thought Leadership"
    - "Interactive Content"
    - "Visual Stories"
    - "Expert Interviews"
```

## Output Format
```json
{
  "generation_date": "2024-01-15",
  "ideas": [
    {
      "id": "IDEA-001",
      "title": "5 AI Trends Reshaping Enterprise Strategy in 2024",
      "type": "trend_analysis",
      "hook": "While everyone talks about AI, these 5 trends are quietly transforming how enterprises operate...",
      "target_audience": "C-Suite Executives",
      "content_pillars": ["Innovation", "Thought Leadership"],
      "trending_connection": "AI Regulation Update",
      "estimated_engagement": "high",
      "format_suggestions": [
        "LinkedIn Article",
        "Infographic",
        "Video Script"
      ],
      "key_points": [
        "Trend 1: Autonomous AI Agents",
        "Trend 2: Edge AI Computing",
        "Trend 3: AI Governance Frameworks"
      ],
      "cta": "Share your biggest AI challenge in the comments"
    }
  ],
  "content_series": [
    {
      "series_name": "AI Transformation Tuesdays",
      "episodes": 8,
      "theme": "Weekly deep-dives into AI implementation"
    }
  ],
  "experimental_ideas": [
    {
      "concept": "AI-Generated Content Challenge",
      "description": "Invite audience to guess which content is AI vs human created",
      "risk_level": "medium",
      "potential_roi": "high"
    }
  ]
}
```

## Creativity Algorithms
```python
creative_techniques = {
    "SCAMPER": "Substitute, Combine, Adapt, Modify, Eliminate, Reverse",
    "Mind_Mapping": "Central topic with radiating connections",
    "Opposite_Thinking": "What would the opposite approach be?",
    "Analogy": "How would another industry solve this?",
    "Constraint_Addition": "What if we had only 1 minute/image/word?"
}
```

## Quality Filters
- **Relevance Score**: Must align with strategy (>7/10)
- **Uniqueness Check**: Not published in last 90 days
- **Engagement Potential**: Based on historical data
- **Feasibility**: Can be created with available resources
- **Trend Alignment**: Connects to current conversations

## Tone Guidelines
Adhere to the shared tone of voice defined in ../agents/tone-of-voice.md: authoritative, innovative, collaborative, value-oriented. Ensure all generated ideas and outputs reflect this tone, providing data-backed, forward-thinking concepts that encourage engagement and align with Oracle AI CoE branding.
