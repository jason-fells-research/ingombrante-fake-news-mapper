#!/usr/bin/env python3
"""
Quick demo runner for the fake news detection system.
Run this to see the pattern analysis in action.
"""

from src.data_loader import NewsDataLoader
from src.pattern_analyzer import PatternAnalyzer
from src.trainer import CriticalThinkingTrainer

def main():
    """Run a quick demo of the fake news detection system."""
    print("🎯 Fake News Pattern Detection Demo")
    print("=" * 40)

    # Initialize components
    loader = NewsDataLoader()
    analyzer = PatternAnalyzer()
    trainer = CriticalThinkingTrainer()

    # Load sample articles
    print("📰 Loading sample articles...")
    articles_df = loader.load_sample_articles()
    print(f"   Loaded {len(articles_df)} articles")

    # Analyze each article
    print("\n🔍 Analyzing articles...")
    for idx, article in articles_df.iterrows():
        print(f"\n📄 Article {idx + 1}: {article['title']}")
        print(f"   Source: {article['source']}")

        analysis = analyzer.analyze_article(
            article['title'],
            article['content'],
            article['source']
        )

        credibility = analysis['overall_score']
        sensationalism = analysis['title_analysis']['sensationalism_score']

        print(f"   📊 Credibility Score: {credibility:.3f}")
        print(f"   🎭 Sensationalism: {sensationalism:.3f}")

        actual_status = "FABRICATED" if article['is_fabricated'] else "REAL"
        predicted_fake = credibility < 0.5
        predicted_status = "FABRICATED" if predicted_fake else "REAL"

        correct = (actual_status == predicted_status)
        status_icon = "✅" if correct else "❌"

        print(f"   🎯 Actual: {actual_status}")
        print(f"   🤖 Predicted: {predicted_status} {status_icon}")

    # Run a training session
    print("\n🎮 Running training session...")
    session = trainer.start_training_session(num_articles=3)

    print(f"   Session #{session['session_id']} completed")
    print(f"   Articles analyzed: {session['total_possible']}")

    print("\n💡 Key patterns to watch for:")
    print("   🔴 Fabricated news often has:")
    print("      • Sensational headlines with caps and exclamation marks")
    print("      • Vague or anonymous sources")
    print("      • Emotional language designed to provoke")
    print("      • Unverifiable claims")

    print("   🟢 Real news typically has:")
    print("      • Specific, named sources and citations")
    print("      • Balanced, informative tone")
    print("      • Verifiable facts and data")
    print("      • Established publication sources")

    print(f"\n🚀 Next steps:")
    print("   • Run 'jupyter notebook' and open notebooks/demo_walkthrough.ipynb")
    print("   • Or explore notebooks/pattern_exploration.ipynb for advanced analysis")
    print("   • Add your own articles to tests/fixtures/sample_articles.json")

if __name__ == "__main__":
    main()