"""
Visualization tools for displaying fake news patterns and analysis results.
Creates charts and graphs to help users understand detection patterns.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import List, Dict
from wordcloud import WordCloud


class PatternVisualizer:
    """Create visualizations for fake news pattern analysis."""

    def __init__(self):
        # Set up plotting style
        plt.style.use('default')
        sns.set_palette("husl")

    def plot_credibility_scores(self, articles_data: List[Dict], save_path: str = None):
        """Plot credibility scores for a set of articles."""
        df = pd.DataFrame(articles_data)

        fig, ax = plt.subplots(figsize=(10, 6))

        # Separate real and fake articles
        real_articles = df[df['is_fabricated'] == False]
        fake_articles = df[df['is_fabricated'] == True]

        ax.scatter(range(len(real_articles)), real_articles['credibility_score'],
                  label='Real News', alpha=0.7, s=100)
        ax.scatter(range(len(fake_articles)), fake_articles['credibility_score'],
                  label='Fabricated News', alpha=0.7, s=100)

        ax.set_xlabel('Article Index')
        ax.set_ylabel('Credibility Score')
        ax.set_title('Credibility Scores: Real vs Fabricated News')
        ax.legend()
        ax.grid(True, alpha=0.3)

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def plot_pattern_comparison(self, analysis_results: Dict, save_path: str = None):
        """Create a radar chart comparing different analysis metrics."""
        metrics = ['Title Sensationalism', 'Credibility Markers', 'Source Quality', 'Content Quality']

        # Extract values for plotting (normalize to 0-1 scale)
        title_score = analysis_results.get('title_analysis', {}).get('sensationalism_score', 0)
        content_markers = min(analysis_results.get('content_analysis', {}).get('credibility_markers', 0) / 5, 1)
        source_quality = 1 - (1 if analysis_results.get('source_analysis', {}).get('has_suspicious_domain') else 0)
        content_quality = analysis_results.get('overall_score', 0.5)

        values = [1 - title_score, content_markers, source_quality, content_quality]  # Invert title score

        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))

        angles = [i * 2 * 3.14159 / len(metrics) for i in range(len(metrics))]
        angles += angles[:1]  # Complete the circle
        values += values[:1]  # Complete the circle

        ax.plot(angles, values, 'o-', linewidth=2, label='Article Analysis')
        ax.fill(angles, values, alpha=0.25)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(metrics)
        ax.set_ylim(0, 1)
        ax.set_title('Article Pattern Analysis', size=16, pad=20)

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def create_word_cloud(self, text_content: str, title: str = "Word Cloud", save_path: str = None):
        """Generate a word cloud from text content."""
        if not text_content:
            print("No text content provided for word cloud")
            return None

        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            max_words=100,
            colormap='viridis'
        ).generate(text_content)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        ax.set_title(title, fontsize=16, pad=20)

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def plot_training_progress(self, training_history: List[Dict], save_path: str = None):
        """Plot training session progress over time."""
        if not training_history:
            print("No training history available")
            return None

        sessions = [session['session_id'] for session in training_history]
        scores = [session['score'] / session['total_possible'] for session in training_history]

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.plot(sessions, scores, 'o-', linewidth=2, markersize=8)
        ax.set_xlabel('Training Session')
        ax.set_ylabel('Accuracy')
        ax.set_title('Critical Thinking Training Progress')
        ax.set_ylim(0, 1)
        ax.grid(True, alpha=0.3)

        # Add trend line
        if len(sessions) > 1:
            z = pd.Series(scores).rolling(window=2).mean()
            ax.plot(sessions, z, '--', alpha=0.7, label='Trend')
            ax.legend()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def create_pattern_summary_chart(self, multiple_analyses: List[Dict], save_path: str = None):
        """Create a summary chart comparing patterns across multiple articles."""
        metrics_data = []

        for i, analysis in enumerate(multiple_analyses):
            metrics_data.append({
                'Article': f'Article {i+1}',
                'Credibility Score': analysis.get('overall_score', 0),
                'Title Sensationalism': analysis.get('title_analysis', {}).get('sensationalism_score', 0),
                'Credibility Markers': min(analysis.get('content_analysis', {}).get('credibility_markers', 0) / 3, 1),
                'Vague Sources': min(analysis.get('content_analysis', {}).get('vague_sources', 0) / 3, 1)
            })

        df = pd.DataFrame(metrics_data)

        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle('Pattern Analysis Summary', fontsize=16)

        # Credibility scores
        axes[0,0].bar(df['Article'], df['Credibility Score'])
        axes[0,0].set_title('Credibility Scores')
        axes[0,0].set_ylabel('Score')

        # Title sensationalism
        axes[0,1].bar(df['Article'], df['Title Sensationalism'])
        axes[0,1].set_title('Title Sensationalism')
        axes[0,1].set_ylabel('Score')

        # Credibility markers
        axes[1,0].bar(df['Article'], df['Credibility Markers'])
        axes[1,0].set_title('Credibility Markers')
        axes[1,0].set_ylabel('Normalized Count')

        # Vague sources
        axes[1,1].bar(df['Article'], df['Vague Sources'])
        axes[1,1].set_title('Vague Sources')
        axes[1,1].set_ylabel('Normalized Count')

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig