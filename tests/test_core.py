import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.data_loader import NewsDataLoader
from src.pattern_analyzer import PatternAnalyzer
from src.trainer import CriticalThinkingTrainer


class TestDataLoader:
    def test_load_sample_articles(self):
        loader = NewsDataLoader()
        df = loader.load_sample_articles()

        assert len(df) > 0
        assert 'title' in df.columns
        assert 'content' in df.columns
        assert 'is_fabricated' in df.columns

    def test_validate_article_format(self):
        loader = NewsDataLoader()

        valid_article = {
            "title": "Test Title",
            "content": "Test content",
            "source": "Test Source",
            "is_fabricated": False
        }

        invalid_article = {
            "title": "Test Title",
            "content": "Test content"
        }

        assert loader.validate_article_format(valid_article) == True
        assert loader.validate_article_format(invalid_article) == False


class TestPatternAnalyzer:
    def test_analyze_article(self):
        analyzer = PatternAnalyzer()

        result = analyzer.analyze_article(
            "Test Title",
            "Test content with credible sources according to research.",
            "Test Source"
        )

        assert 'title_analysis' in result
        assert 'content_analysis' in result
        assert 'source_analysis' in result
        assert 'overall_score' in result
        assert 0 <= result['overall_score'] <= 1

    def test_sensationalism_detection(self):
        analyzer = PatternAnalyzer()

        sensational_title = "SHOCKING!!! You Won't BELIEVE This!!!"
        normal_title = "Local Council Meets to Discuss Budget"

        sensational_result = analyzer._analyze_title(sensational_title)
        normal_result = analyzer._analyze_title(normal_title)

        assert sensational_result['sensationalism_score'] > normal_result['sensationalism_score']


class TestCriticalThinkingTrainer:
    def test_start_training_session(self):
        trainer = CriticalThinkingTrainer()

        session = trainer.start_training_session(num_articles=2)

        assert 'session_id' in session
        assert 'articles' in session
        assert len(session['articles']) <= 2
        assert 'score' in session

    def test_generate_hints(self):
        trainer = CriticalThinkingTrainer()

        # Mock analysis with high sensationalism
        analysis = {
            'title_analysis': {'sensationalism_score': 0.8, 'exclamation_marks': 3},
            'content_analysis': {'credibility_markers': 0, 'vague_sources': 2},
            'source_analysis': {'has_suspicious_domain': True}
        }

        hints = trainer._generate_hints(analysis)

        assert len(hints) > 0
        assert any("sensationalism" in hint.lower() for hint in hints)