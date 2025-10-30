"""
Interactive training exercises for developing critical thinking skills.
Provides guided practice in identifying fake news patterns.
"""

import random
from typing import List, Dict, Tuple
from src.data_loader import NewsDataLoader
from src.pattern_analyzer import PatternAnalyzer


class CriticalThinkingTrainer:
    """Interactive trainer for fake news detection skills."""

    def __init__(self):
        self.data_loader = NewsDataLoader()
        self.analyzer = PatternAnalyzer()
        self.training_history = []

    def start_training_session(self, num_articles: int = 3) -> Dict:
        """Start an interactive training session."""
        articles_df = self.data_loader.load_sample_articles()

        # Select random articles for training
        selected_articles = articles_df.sample(n=min(num_articles, len(articles_df)))

        session_results = {
            "session_id": len(self.training_history) + 1,
            "articles": [],
            "score": 0,
            "total_possible": len(selected_articles)
        }

        for _, article in selected_articles.iterrows():
            exercise_result = self._create_exercise(article)
            session_results["articles"].append(exercise_result)

        self.training_history.append(session_results)
        return session_results

    def _create_exercise(self, article) -> Dict:
        """Create a training exercise from an article."""
        analysis = self.analyzer.analyze_article(
            article['title'],
            article['content'],
            article['source']
        )

        return {
            "article_id": article['id'],
            "title": article['title'],
            "content": article['content'][:200] + "..." if len(article['content']) > 200 else article['content'],
            "source": article['source'],
            "actual_status": "fabricated" if article['is_fabricated'] else "real",
            "analysis_hints": self._generate_hints(analysis),
            "credibility_score": analysis['overall_score']
        }

    def _generate_hints(self, analysis: Dict) -> List[str]:
        """Generate helpful hints based on analysis results."""
        hints = []

        # Title analysis hints
        title_analysis = analysis.get('title_analysis', {})
        if title_analysis.get('sensationalism_score', 0) > 0.5:
            hints.append("⚠️ Title shows signs of sensationalism (excessive caps, suspicious phrases)")

        if title_analysis.get('exclamation_marks', 0) > 1:
            hints.append("❗ Multiple exclamation marks may indicate emotional manipulation")

        # Content analysis hints
        content_analysis = analysis.get('content_analysis', {})
        if content_analysis.get('credibility_markers', 0) > 2:
            hints.append("✅ Article cites multiple credible sources or studies")

        if content_analysis.get('vague_sources', 0) > 1:
            hints.append("🔍 Article relies on vague or anonymous sources")

        # Source analysis hints
        source_analysis = analysis.get('source_analysis', {})
        if source_analysis.get('has_suspicious_domain'):
            hints.append("🌐 Source domain may not be from established media")

        if source_analysis.get('has_established_pattern'):
            hints.append("📰 Source name follows established media patterns")

        return hints

    def get_learning_summary(self) -> Dict:
        """Generate a summary of learning progress."""
        if not self.training_history:
            return {"message": "No training sessions completed yet"}

        total_articles = sum(session['total_possible'] for session in self.training_history)
        total_correct = sum(session['score'] for session in self.training_history)

        return {
            "total_sessions": len(self.training_history),
            "total_articles_reviewed": total_articles,
            "accuracy": total_correct / total_articles if total_articles > 0 else 0,
            "latest_session_score": self.training_history[-1]['score'],
            "improvement_tips": self._generate_improvement_tips()
        }

    def _generate_improvement_tips(self) -> List[str]:
        """Generate personalized improvement tips based on history."""
        tips = [
            "Look for specific source citations and named experts",
            "Be suspicious of emotionally charged language in headlines",
            "Check if claims are supported by verifiable evidence",
            "Consider the source's reputation and domain",
            "Look for multiple independent confirmations of claims"
        ]

        # Return 3 random tips for now
        return random.sample(tips, 3)