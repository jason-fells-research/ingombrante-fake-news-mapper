"""
Pattern analyzer for identifying fabrication indicators in news articles.
Analyzes text features that commonly distinguish real from fabricated news.
"""

import re
import string
from typing import Dict, List, Tuple
from collections import Counter
import textstat


class PatternAnalyzer:
    """Analyze text patterns that may indicate fabricated news."""

    def __init__(self):
        self.suspicious_phrases = [
            "shocking", "you won't believe", "scientists hate him",
            "doctors don't want you to know", "secret revealed",
            "breakthrough study", "undisclosed", "anonymous source"
        ]

        self.credibility_markers = [
            "according to", "data shows", "research indicates",
            "study published in", "expert analysis", "official statement"
        ]

    def analyze_article(self, title: str, content: str, source: str) -> Dict:
        """Perform comprehensive pattern analysis on an article."""
        return {
            "title_analysis": self._analyze_title(title),
            "content_analysis": self._analyze_content(content),
            "source_analysis": self._analyze_source(source),
            "overall_score": self._calculate_credibility_score(title, content, source)
        }

    def _analyze_title(self, title: str) -> Dict:
        """Analyze title for sensationalism and suspicious patterns."""
        title_lower = title.lower()

        # Check for excessive capitalization
        caps_ratio = sum(1 for c in title if c.isupper()) / len(title) if title else 0

        # Check for suspicious phrases
        suspicious_count = sum(1 for phrase in self.suspicious_phrases if phrase in title_lower)

        # Check for excessive punctuation
        exclamation_count = title.count('!')

        return {
            "caps_ratio": caps_ratio,
            "suspicious_phrases": suspicious_count,
            "exclamation_marks": exclamation_count,
            "sensationalism_score": self._calculate_sensationalism_score(caps_ratio, suspicious_count, exclamation_count)
        }

    def _analyze_content(self, content: str) -> Dict:
        """Analyze content for writing quality and credibility markers."""
        if not content:
            return {"error": "No content provided"}

        # Basic readability metrics
        reading_ease = textstat.flesch_reading_ease(content)
        grade_level = textstat.flesch_kincaid_grade(content)

        # Count credibility markers
        content_lower = content.lower()
        credibility_markers = sum(1 for marker in self.credibility_markers if marker in content_lower)

        # Analyze sentence structure
        sentences = content.split('.')
        avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0

        # Check for vague sourcing
        vague_sources = self._count_vague_sources(content_lower)

        return {
            "reading_ease": reading_ease,
            "grade_level": grade_level,
            "credibility_markers": credibility_markers,
            "avg_sentence_length": avg_sentence_length,
            "vague_sources": vague_sources
        }

    def _analyze_source(self, source: str) -> Dict:
        """Analyze source credibility indicators."""
        source_lower = source.lower()

        # Check for suspicious domain patterns
        suspicious_domains = [".net", "news.com", "realtruth", "totallytrue"]
        has_suspicious_domain = any(domain in source_lower for domain in suspicious_domains)

        # Check for established media patterns
        established_patterns = ["times", "post", "herald", "tribune", "gazette"]
        has_established_pattern = any(pattern in source_lower for pattern in established_patterns)

        return {
            "has_suspicious_domain": has_suspicious_domain,
            "has_established_pattern": has_established_pattern,
            "source_length": len(source)
        }

    def _count_vague_sources(self, content: str) -> int:
        """Count vague or unverifiable source references."""
        vague_patterns = [
            "anonymous", "undisclosed", "sources say", "reports suggest",
            "it is believed", "allegedly", "unnamed source"
        ]
        return sum(content.count(pattern) for pattern in vague_patterns)

    def _calculate_sensationalism_score(self, caps_ratio: float, suspicious_phrases: int, exclamations: int) -> float:
        """Calculate sensationalism score (0-1, higher = more sensational)."""
        score = 0.0
        score += min(caps_ratio * 2, 0.4)  # Cap contribution at 0.4
        score += min(suspicious_phrases * 0.3, 0.4)  # Cap at 0.4
        score += min(exclamations * 0.1, 0.2)  # Cap at 0.2
        return min(score, 1.0)

    def _calculate_credibility_score(self, title: str, content: str, source: str) -> float:
        """Calculate overall credibility score (0-1, higher = more credible)."""
        title_analysis = self._analyze_title(title)
        content_analysis = self._analyze_content(content)
        source_analysis = self._analyze_source(source)

        # Start with neutral score
        score = 0.5

        # Adjust based on title sensationalism (negative impact)
        score -= title_analysis["sensationalism_score"] * 0.3

        # Adjust based on credibility markers (positive impact)
        if "credibility_markers" in content_analysis:
            score += min(content_analysis["credibility_markers"] * 0.1, 0.2)

        # Adjust based on source analysis
        if source_analysis["has_suspicious_domain"]:
            score -= 0.2
        if source_analysis["has_established_pattern"]:
            score += 0.1

        # Adjust based on vague sourcing (negative impact)
        if "vague_sources" in content_analysis:
            score -= min(content_analysis["vague_sources"] * 0.05, 0.2)

        return max(0.0, min(1.0, score))