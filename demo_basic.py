#!/usr/bin/env python3
"""
Minimal demo that works without external dependencies.
Shows the basic concept before installing requirements.
"""

def basic_demo():
    """Run a basic demo without external dependencies."""
    print("🎯 Fake News Detection - Basic Demo")
    print("=" * 40)

    # Sample articles (embedded for demo)
    articles = [
        {
            "title": "Local Library Opens New Reading Program for Children",
            "source": "Springfield Daily News",
            "is_fabricated": False
        },
        {
            "title": "SHOCKING: Scientists Discover Cats Can Actually Speak Human Language",
            "source": "TotallyRealNews.net",
            "is_fabricated": True
        }
    ]

    print("📰 Sample articles loaded:")
    for i, article in enumerate(articles, 1):
        status = "🔴 FABRICATED" if article['is_fabricated'] else "🟢 REAL"
        print(f"  {i}. {status}: {article['title']}")
        print(f"     Source: {article['source']}")

    print("\n🔍 Basic pattern analysis:")

    for article in articles:
        print(f"\n📄 Analyzing: {article['title'][:50]}...")

        # Simple heuristic analysis
        title = article['title']
        source = article['source']

        # Check for suspicious patterns
        suspicious_words = ['shocking', 'secret', 'doctors hate', 'you won\'t believe']
        caps_count = sum(1 for c in title if c.isupper())
        exclamation_count = title.count('!')

        suspicious_score = 0
        if any(word in title.lower() for word in suspicious_words):
            suspicious_score += 0.3
        if caps_count > len(title) * 0.2:  # >20% caps
            suspicious_score += 0.3
        if exclamation_count > 1:
            suspicious_score += 0.2
        if '.net' in source.lower() or 'real' in source.lower():
            suspicious_score += 0.2

        credibility = 1.0 - suspicious_score

        print(f"   📊 Credibility Score: {credibility:.2f}")
        print(f"   🎭 Suspicious Patterns: {suspicious_score:.2f}")

        actual = "FABRICATED" if article['is_fabricated'] else "REAL"
        predicted = "FABRICATED" if credibility < 0.5 else "REAL"
        correct = "✅" if actual == predicted else "❌"

        print(f"   🎯 Actual: {actual}, Predicted: {predicted} {correct}")

    print("\n💡 Key patterns detected:")
    print("   🔴 Red flags: ALL CAPS, multiple !!!, suspicious sources")
    print("   🟢 Trust signals: Balanced tone, established news sources")

    print("\n🚀 Next steps:")
    print("   1. Install dependencies: pip install -r requirements.txt")
    print("   2. Run full demo: python demo.py")
    print("   3. Try interactive notebooks: jupyter notebook")

if __name__ == "__main__":
    basic_demo()