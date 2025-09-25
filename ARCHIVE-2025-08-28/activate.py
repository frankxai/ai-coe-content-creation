#!/usr/bin/env python3
"""
Content Magic - Simplified Activation Script
Create world-class content in 15 minutes or less
"""

import json
import argparse
import logging
from datetime import datetime
import os
import sys
import random
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger('ContentMagic')

class ContentMagic:
    """Simplified Content Creation System"""
    
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.active_dir = self.base_path / 'ACTIVE'
        self.templates_dir = self.base_path / 'templates'
        self.prompts_dir = self.base_path / 'prompts'
        
        # Ensure directories exist
        self.active_dir.mkdir(exist_ok=True)
        
        # Viral hooks database
        self.viral_hooks = [
            "Your competitor just automated {percentage}% of operations. You're still in meetings.",
            "The ${amount}M decision that {percentage}% of {audience} miss...",
            "After analyzing {number}+ {items}, I found the pattern everyone ignores...",
            "In {timeframe}, this won't matter. Here's what will...",
            "{common_belief}? Dead wrong. Here's the truth...",
            "While you're {activity}, industry leaders are already {achievement}...",
            "The {industry} hack that's {result} (and why no one talks about it)",
        ]
        
        # High-value topics
        self.trending_topics = [
            "Agentic AI Workflows",
            "Multi-Modal AI Systems", 
            "AI Cost Optimization",
            "Enterprise AI Security",
            "RAG Architecture Patterns",
            "AI Governance Frameworks",
            "Prompt Engineering at Scale",
            "AI Team Productivity",
            "Vector Database Selection",
            "LLM Fine-Tuning Strategies"
        ]
        
    def create_content(self, topic=None, platforms=['all'], mode='full'):
        """Main content creation pipeline"""
        
        logger.info("🚀 Content Magic Activated")
        logger.info("=" * 50)
        
        # Step 1: Topic Selection
        if not topic:
            topic = self.select_topic()
        logger.info(f"📝 Topic: {topic}")
        
        # Step 2: Research Phase (simulated for demo)
        logger.info("🔍 Researching trends...")
        research = self.research_phase(topic)
        
        # Step 3: Ideation Phase
        logger.info("💡 Generating viral ideas...")
        ideas = self.ideation_phase(topic, research)
        
        # Step 4: Content Creation
        logger.info("✍️  Creating content...")
        content = self.creation_phase(topic, ideas, platforms)
        
        # Step 5: Quality Check
        logger.info("✅ Running quality checks...")
        quality_score = self.quality_check(content)
        
        # Step 6: Package and Save
        logger.info("📦 Packaging outputs...")
        output_files = self.save_outputs(content, topic)
        
        # Summary
        logger.info("=" * 50)
        logger.info("✨ Content Creation Complete!")
        logger.info(f"📊 Quality Score: {quality_score}/10")
        logger.info(f"📁 Files saved to: ACTIVE/")
        
        for file in output_files:
            logger.info(f"   - {file}")
        
        return {
            'status': 'success',
            'topic': topic,
            'quality_score': quality_score,
            'files': output_files,
            'next_steps': [
                "1. Review content in ACTIVE/today-content.html",
                "2. Copy LinkedIn post from ACTIVE/today-linkedin.txt",
                "3. Post and track engagement"
            ]
        }
    
    def select_topic(self):
        """Auto-select trending topic"""
        return random.choice(self.trending_topics)
    
    def research_phase(self, topic):
        """Simulate research phase"""
        return {
            'trending': True,
            'competition': 'low',
            'opportunity': 'high',
            'keywords': self.extract_keywords(topic),
            'insights': [
                f"87% of enterprises struggle with {topic}",
                f"Early adopters see 3x ROI from {topic}",
                f"Oracle leads in {topic} implementation"
            ]
        }
    
    def extract_keywords(self, topic):
        """Extract SEO keywords from topic"""
        words = topic.lower().split()
        keywords = words + ['oracle', 'ai', 'enterprise', 'transformation']
        return list(set(keywords))
    
    def ideation_phase(self, topic, research):
        """Generate content ideas"""
        ideas = []
        for i in range(3):
            hook_template = random.choice(self.viral_hooks)
            hook = self.fill_hook_template(hook_template, topic)
            ideas.append({
                'hook': hook,
                'angle': f"Unique perspective on {topic}",
                'score': round(random.uniform(8.0, 9.8), 1)
            })
        return sorted(ideas, key=lambda x: x['score'], reverse=True)
    
    def fill_hook_template(self, template, topic):
        """Fill in hook template with dynamic values"""
        replacements = {
            '{percentage}': str(random.randint(60, 95)),
            '{amount}': str(random.randint(5, 50)),
            '{audience}': random.choice(['CTOs', 'enterprises', 'IT leaders']),
            '{number}': str(random.randint(500, 2000)),
            '{items}': random.choice(['implementations', 'companies', 'projects']),
            '{timeframe}': random.choice(['6 months', '2025', 'next quarter']),
            '{common_belief}': f"Everyone thinks {topic} is complex",
            '{activity}': 'evaluating options',
            '{achievement}': f'deploying {topic} at scale',
            '{industry}': 'enterprise AI',
            '{result}': '10x productivity'
        }
        
        result = template
        for key, value in replacements.items():
            result = result.replace(key, value)
        return result
    
    def creation_phase(self, topic, ideas, platforms):
        """Create content for specified platforms"""
        
        best_idea = ideas[0]
        content = {}
        
        # LinkedIn Post
        if 'all' in platforms or 'linkedin' in platforms:
            content['linkedin'] = self.create_linkedin_post(topic, best_idea)
        
        # Twitter Thread
        if 'all' in platforms or 'twitter' in platforms or 'x' in platforms:
            content['twitter'] = self.create_twitter_thread(topic, best_idea)
        
        # Blog Outline
        if 'all' in platforms or 'blog' in platforms:
            content['blog'] = self.create_blog_outline(topic, best_idea)
        
        return content
    
    def create_linkedin_post(self, topic, idea):
        """Generate LinkedIn post"""
        post = f"""{idea['hook']}

Here's what industry leaders know about {topic}:

The game has changed. While traditional approaches focus on evaluation and planning, innovators are already implementing and iterating.

Three insights from architecting {topic} solutions:

→ Speed beats perfection: Launch MVP in weeks, not months
→ Integration is everything: Native Oracle Cloud advantage
→ Data drives decisions: Real-time analytics from day one

I've seen companies transform their operations with {topic}:
• 40% cost reduction in 6 months
• 3x productivity improvement
• 95% accuracy in automated decisions

The breakthrough? Oracle's integrated AI platform on OCI.

Unlike pieced-together solutions, you get:
✓ Enterprise security built-in
✓ Seamless data pipeline integration  
✓ Pre-trained industry models
✓ Predictable scaling costs

The question isn't whether to adopt {topic}.
It's whether you'll lead or follow.

What's your {topic} strategy for 2025?

#AI #OracleCloud #DigitalTransformation #Innovation #EnterpriseTech"""
        
        return post
    
    def create_twitter_thread(self, topic, idea):
        """Generate Twitter/X thread"""
        thread = [
            f"🧵 {idea['hook']}",
            f"The truth about {topic}? Most companies are doing it wrong.",
            f"Winners focus on 3 things:\n\n1. Speed over perfection\n2. Integration over isolation\n3. Data over assumptions",
            f"Real results from {topic} implementation:\n\n• 40% cost reduction\n• 3x productivity boost\n• 95% automation accuracy\n\nIn just 6 months.",
            f"The secret sauce? Oracle's AI on OCI.\n\nEnterprise-ready from day one.",
            f"Stop evaluating. Start implementing.\n\nYour competition already has.\n\n/end"
        ]
        return thread
    
    def create_blog_outline(self, topic, idea):
        """Generate blog article outline"""
        outline = {
            'title': f"The Executive Guide to {topic}: From Strategy to Implementation",
            'hook': idea['hook'],
            'sections': [
                {
                    'heading': 'The Current State of ' + topic,
                    'points': ['Market analysis', 'Common challenges', 'Opportunity size'],
                    'words': 400
                },
                {
                    'heading': 'Why Oracle Leads in ' + topic,
                    'points': ['Platform advantages', 'Integration benefits', 'Security features'],
                    'words': 500
                },
                {
                    'heading': 'Implementation Roadmap',
                    'points': ['Week 1-2: Assessment', 'Week 3-4: Pilot', 'Week 5-8: Scale'],
                    'words': 600
                },
                {
                    'heading': 'Success Metrics and ROI',
                    'points': ['KPIs to track', 'Expected timeline', 'Case studies'],
                    'words': 400
                },
                {
                    'heading': 'Your Next Steps',
                    'points': ['Quick wins', 'Resource requirements', 'Getting started'],
                    'words': 300
                }
            ],
            'total_words': 2200,
            'keywords': ['Oracle', topic, 'AI', 'enterprise', 'implementation']
        }
        return outline
    
    def quality_check(self, content):
        """Assess content quality"""
        scores = []
        
        # Check hook strength (simplified)
        if content.get('linkedin'):
            hook_score = 9.0 if any(char in content['linkedin'][:100] for char in ['?', '!', '$', '%']) else 7.5
            scores.append(hook_score)
        
        # Check value density
        value_score = 8.5  # Simplified for demo
        scores.append(value_score)
        
        # Check SEO optimization
        seo_score = 8.8  # Simplified for demo
        scores.append(seo_score)
        
        return round(sum(scores) / len(scores), 1) if scores else 8.0
    
    def save_outputs(self, content, topic):
        """Save content to ACTIVE directory"""
        timestamp = datetime.now().strftime('%Y-%m-%d')
        files_created = []
        
        # Save LinkedIn post
        if 'linkedin' in content:
            linkedin_file = self.active_dir / 'today-linkedin.txt'
            with open(linkedin_file, 'w', encoding='utf-8') as f:
                f.write(content['linkedin'])
            files_created.append('today-linkedin.txt')
        
        # Save Twitter thread
        if 'twitter' in content:
            twitter_file = self.active_dir / 'today-twitter.txt'
            with open(twitter_file, 'w', encoding='utf-8') as f:
                for i, tweet in enumerate(content['twitter'], 1):
                    f.write(f"Tweet {i}:\n{tweet}\n\n")
            files_created.append('today-twitter.txt')
        
        # Save blog outline
        if 'blog' in content:
            blog_file = self.active_dir / 'today-blog-outline.json'
            with open(blog_file, 'w', encoding='utf-8') as f:
                json.dump(content['blog'], f, indent=2)
            files_created.append('today-blog-outline.json')
        
        # Create HTML dashboard
        self.create_dashboard(content, topic, timestamp)
        files_created.append('today-content.html')
        
        return files_created
    
    def create_dashboard(self, content, topic, timestamp):
        """Create HTML dashboard for all content"""
        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Content Magic - {topic}</title>
    <style>
        body {{ font-family: 'Inter', sans-serif; background: #0a0e27; color: #e4e8f1; padding: 20px; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        h1 {{ color: #667eea; }}
        .card {{ background: rgba(255,255,255,0.05); border-radius: 10px; padding: 20px; margin: 20px 0; }}
        .linkedin {{ border-left: 3px solid #0077b5; }}
        .twitter {{ border-left: 3px solid #1da1f2; }}
        .blog {{ border-left: 3px solid #667eea; }}
        pre {{ white-space: pre-wrap; line-height: 1.6; }}
        .copy-btn {{ background: #667eea; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📱 Today's Content: {topic}</h1>
        <p>Generated: {timestamp}</p>
        """
        
        if 'linkedin' in content:
            html += f"""
        <div class="card linkedin">
            <h2>LinkedIn Post</h2>
            <pre>{content['linkedin']}</pre>
            <button class="copy-btn" onclick="navigator.clipboard.writeText(this.previousElementSibling.textContent)">Copy to Clipboard</button>
        </div>"""
        
        if 'twitter' in content:
            html += """
        <div class="card twitter">
            <h2>Twitter/X Thread</h2>"""
            for i, tweet in enumerate(content['twitter'], 1):
                html += f"<p><strong>Tweet {i}:</strong> {tweet}</p>"
            html += """</div>"""
        
        if 'blog' in content:
            html += f"""
        <div class="card blog">
            <h2>Blog Outline</h2>
            <h3>{content['blog']['title']}</h3>
            <ul>"""
            for section in content['blog']['sections']:
                html += f"<li><strong>{section['heading']}</strong> ({section['words']} words)</li>"
            html += """</ul>
        </div>"""
        
        html += """
    </div>
</body>
</html>"""
        
        dashboard_file = self.active_dir / 'today-content.html'
        with open(dashboard_file, 'w', encoding='utf-8') as f:
            f.write(html)

def main():
    parser = argparse.ArgumentParser(
        description='Content Magic - Create world-class content in minutes',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python activate.py                     # Full auto mode
  python activate.py --topic "AI Agents" # Specific topic
  python activate.py --platform linkedin # LinkedIn only
  python activate.py --mode quick        # Fast mode
        """
    )
    
    parser.add_argument('--topic', help='Content topic (auto-selected if not provided)')
    parser.add_argument('--platforms', nargs='+', default=['all'], 
                       choices=['all', 'linkedin', 'twitter', 'x', 'blog'],
                       help='Target platforms')
    parser.add_argument('--mode', default='full', choices=['full', 'quick', 'test'],
                       help='Execution mode')
    
    args = parser.parse_args()
    
    # Initialize and run
    magic = ContentMagic()
    result = magic.create_content(
        topic=args.topic,
        platforms=args.platforms,
        mode=args.mode
    )
    
    # Exit with appropriate code
    sys.exit(0 if result['status'] == 'success' else 1)

if __name__ == '__main__':
    main()