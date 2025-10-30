"""
Data loader for news articles and training datasets.
Handles parsing, validation, and preprocessing of news content.
"""

import json
import pandas as pd
from typing import List, Dict, Optional
from pathlib import Path


class NewsDataLoader:
    """Load and preprocess news articles for pattern analysis."""

    def __init__(self, data_path: Optional[str] = None):
        self.data_path = Path(data_path) if data_path else Path("tests/fixtures")

    def load_sample_articles(self) -> pd.DataFrame:
        """Load sample articles from fixtures for testing and demos."""
        sample_file = self.data_path / "sample_articles.json"

        if not sample_file.exists():
            # Return demo data if no file exists
            return self._create_demo_data()

        with open(sample_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        return pd.DataFrame(data)

    def _create_demo_data(self) -> pd.DataFrame:
        """Create minimal demo data for immediate testing."""
        demo_articles = [
            {
                "id": "real_1",
                "title": "Local Library Opens New Reading Program for Children",
                "content": "The Springfield Public Library announced today the launch of their new summer reading program. The initiative will provide free books and activities for children aged 5-12 throughout the summer months. Library director Sarah Johnson stated that the program aims to prevent summer learning loss and encourage literacy development.",
                "source": "Springfield Daily News",
                "is_fabricated": False,
                "date": "2025-10-29"
            },
            {
                "id": "fake_1",
                "title": "SHOCKING: Scientists Discover Cats Can Actually Speak Human Language",
                "content": "In a groundbreaking study that will revolutionize pet ownership forever, researchers at an undisclosed university have proven that cats possess the ability to speak fluent human language. Dr. Anonymous claims that cats have been hiding this ability for thousands of years. The study, which cannot be verified due to 'security reasons', suggests that your cat has been judging your life choices all along.",
                "source": "TotallyRealNews.net",
                "is_fabricated": True,
                "date": "2025-10-29"
            },
            {
                "id": "real_2",
                "title": "City Council Approves New Traffic Light Installation",
                "content": "The Springfield City Council voted 6-2 last night to approve the installation of a new traffic light at the intersection of Main Street and Oak Avenue. The decision comes after months of resident complaints about traffic safety at the busy intersection. Installation is expected to begin next month and complete by December.",
                "source": "Springfield Tribune",
                "is_fabricated": False,
                "date": "2025-10-28"
            }
        ]

        return pd.DataFrame(demo_articles)

    def validate_article_format(self, article: Dict) -> bool:
        """Validate that article has required fields."""
        required_fields = ["title", "content", "source", "is_fabricated"]
        return all(field in article for field in required_fields)