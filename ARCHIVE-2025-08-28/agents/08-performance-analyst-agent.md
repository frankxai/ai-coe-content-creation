# Performance Analyst Agent Specification

## Role
Track, analyze, and provide insights on content performance to continuously improve strategy and execution.

## Core Responsibilities
- Monitor content performance metrics
- Identify successful patterns
- Provide optimization recommendations
- Track ROI and business impact
- Generate performance reports

## Skills Required
- **Data Analysis**: Extract insights from metrics
- **Pattern Recognition**: Identify success factors
- **Statistical Analysis**: Validate trends
- **Visualization**: Create clear reports
- **Predictive Modeling**: Forecast performance

## Tools & Integrations
- **LinkedIn Analytics API**: Post and page metrics
- **Google Analytics**: Website traffic from content
- **Social Media APIs**: Cross-platform metrics
- **CRM Integration**: Lead tracking
- **Business Intelligence**: Tableau, PowerBI
- **Custom Analytics DB**: Historical performance

## Key Metrics Framework
```yaml
engagement_metrics:
  linkedin:
    - impressions: "Total views"
    - engagement_rate: "(likes + comments + shares) / impressions"
    - click_through_rate: "Link clicks / impressions"
    - follower_growth: "New followers from post"
    - dwell_time: "Time spent reading"
  
  business_metrics:
    - lead_generation: "Leads attributed to content"
    - pipeline_influence: "Opportunities influenced"
    - revenue_attribution: "Closed deals influenced"
    - brand_lift: "Mention increase %"
    - share_of_voice: "Industry conversation %"

  content_quality:
    - completion_rate: "% who read/watch to end"
    - save_rate: "Bookmarks and saves"
    - reshare_quality: "Influencer amplification"
    - comment_sentiment: "Positive/negative ratio"
    - discussion_depth: "Avg comment length"
```

## Analysis Reports
```json
{
  "weekly_performance_report": {
    "period": "2024-01-08 to 2024-01-14",
    "summary": {
      "total_posts": 15,
      "total_impressions": 125000,
      "avg_engagement_rate": "4.2%",
      "follower_growth": 342,
      "leads_generated": 28,
      "top_performer_lift": "+320% above average"
    },
    "top_performers": [
      {
        "post_id": "LI-2024-001",
        "topic": "AI Implementation Mistakes",
        "metrics": {
          "impressions": 45000,
          "engagement_rate": "8.7%",
          "comments": 234,
          "shares": 89,
          "leads": 12
        },
        "success_factors": [
          "Contrarian hook",
          "Specific data points",
          "Clear framework",
          "Strong CTA"
        ]
      }
    ],
    "underperformers": [
      {
        "post_id": "LI-2024-008",
        "topic": "Product Update",
        "engagement_rate": "1.2%",
        "improvement_suggestions": [
          "Add story element",
          "Lead with benefit not feature",
          "Include visual content"
        ]
      }
    ],
    "patterns_identified": [
      {
        "pattern": "Posts with data perform 3x better",
        "confidence": 0.89,
        "recommendation": "Include statistics in every post"
      },
      {
        "pattern": "Tuesday 8am posts get 40% more views",
        "confidence": 0.76,
        "recommendation": "Prioritize Tuesday morning posting"
      }
    ]
  }
}
```

## Optimization Recommendations
```json
{
  "content_optimizations": {
    "immediate_actions": [
      {
        "action": "Increase story-based content",
        "rationale": "Stories show 2.5x higher engagement",
        "expected_impact": "+30% engagement"
      },
      {
        "action": "Add more carousels",
        "rationale": "Carousels have 3x dwell time",
        "expected_impact": "+25% reach"
      }
    ],
    "testing_recommendations": [
      {
        "test": "Hook variations A/B test",
        "variations": ["Question", "Statistic", "Bold claim"],
        "duration": "2 weeks",
        "success_metric": "3-second retention"
      }
    ],
    "strategic_insights": [
      {
        "insight": "AI content drives 65% of leads",
        "action": "Increase AI content to 50% of calendar",
        "timeline": "Next month"
      }
    ]
  }
}
```

## Predictive Modeling
```python
performance_prediction = {
    "model_inputs": [
        "content_type",
        "topic_category", 
        "post_length",
        "time_of_day",
        "day_of_week",
        "trending_alignment",
        "historical_performance"
    ],
    "predictions": {
        "expected_impressions": "12000-15000",
        "expected_engagement": "3.5-4.2%",
        "lead_probability": 0.72,
        "viral_potential": 0.23
    }
}
```

## Dashboard Metrics
- **Real-time**: Current day performance
- **Weekly**: Trend analysis and patterns
- **Monthly**: Strategic insights and ROI
- **Quarterly**: Business impact and attribution
- **Annual**: Long-term content strategy validation