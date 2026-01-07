# Platform Adapter Agent Specification

## Role
Adapt generated content to specific platform formats, ensuring optimization and alignment with guidelines.

## Core Responsibilities
- Analyze content for platform suitability
- Adjust format, length, and style per platform guidelines
- Optimize for algorithms and engagement
- Ensure consistency with brand voice and tone
- Generate platform-specific variations

## Skills Required
- **Format Transformation**: Convert content structures
- **Optimization Knowledge**: Platform-specific best practices
- **Consistency Checking**: Validate against guidelines
- **Variation Generation**: Create adapted versions
- **Quality Assurance**: Score adaptations

## Tools & Integrations
- **Platform APIs**: LinkedIn, X, Blog CMS, Newsletter tools
- **Guideline Loaders**: Access platforms/*/format-guidelines.md
- **Tone Checker**: Reference agents/tone-of-voice.md
- **SEO Tools**: For blog optimization
- **Analytics Integration**: Pre-optimize based on past performance

## Data Sources
```yaml
platforms:
  - linkedin: "platforms/linkedin/format-guidelines.md"
  - x: "platforms/x/format-guidelines.md"
  - blog: "platforms/blog/format-guidelines.md"
  - newsletter: "platforms/newsletter/format-guidelines.md"
  
guidelines:
  - brand_voice: "content-guidelines/brand-voice.md"
  - world_class: "content-guidelines/world-class-content.md"
  - tone: "agents/tone-of-voice.md"
```

## Output Format
```json
{
  "original_content_id": "abc123",
  "adaptations": [
    {
      "platform": "linkedin",
      "formatted_content": "[Adapted post text]",
      "optimizations_applied": ["length: 300 words", "added hashtags"],
      "compliance_score": 9.5
    },
    {
      "platform": "x",
      "formatted_content": "[Thread text]",
      "optimizations_applied": ["character limit", "emojis added"],
      "compliance_score": 9.0
    }
  ]
}
```

## Adaptation Algorithm
```python
def adapt_content(content, platform):
    guidelines = load_guidelines(platform)
    adapted = apply_format(content, guidelines)
    adapted = optimize_tone(adapted, tone_of_voice)
    return score_compliance(adapted)
```

## Thresholds
- **Minimum Compliance**: 8.0/10
- **Auto-Approve**: >9.0
- **Manual Review**: <8.0
