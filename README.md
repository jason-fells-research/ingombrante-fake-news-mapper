# ingombrante-fake-news-mapper

Train your critical thinking skills by identifying real vs. fabricated news patterns.

## 🎯 What This Does

This interactive tool helps you develop critical thinking skills by analyzing patterns that distinguish real news from fabricated content. It provides:

- **Pattern Analysis**: Automated detection of sensationalism, source credibility, and writing quality indicators
- **Interactive Training**: Guided exercises to practice identifying fake news patterns
- **Visual Learning**: Charts and graphs showing detection patterns
- **Hands-on Experience**: Jupyter notebooks for exploring your own articles

## 🚀 Quick Start

### 1. Setup Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Quick Demo
```bash
python demo.py
```

### 3. Interactive Notebooks
```bash
# Start Jupyter
jupyter notebook

# Then open:
# - notebooks/demo_walkthrough.ipynb (guided demo)
# - notebooks/pattern_exploration.ipynb (advanced analysis)
```

## 📁 Project Structure

```
src/
├── data_loader.py      # Load and validate news articles
├── pattern_analyzer.py # Detect fabrication indicators
├── trainer.py          # Interactive training exercises
└── visualizer.py       # Charts and pattern visualization

notebooks/
├── demo_walkthrough.ipynb    # Interactive demo tutorial
└── pattern_exploration.ipynb # Advanced analysis tools

tests/
├── fixtures/sample_articles.json  # Sample real/fake articles
└── test_core.py                   # Unit tests

demo.py                 # Quick command-line demo
requirements.txt        # Python dependencies
```

## 🔍 Key Detection Patterns

### Red Flags (Suspicious):
- **Sensational headlines** with excessive caps, exclamation marks
- **Vague sources** like "anonymous experts" or "undisclosed study"
- **Emotional manipulation** designed to provoke rather than inform
- **Unverifiable claims** about "secret research" or "suppressed information"

### Trust Indicators (Credible):
- **Named sources** with specific experts, institutions, citations
- **Balanced tone** that informs rather than inflames
- **Verifiable facts** including dates, locations, statistics
- **Established sources** from recognized news organizations

## 🛠️ Adding Your Own Data

Add articles to `tests/fixtures/sample_articles.json`:

```json
{
  "id": "custom_1",
  "title": "Your Article Title",
  "content": "Full article text...",
  "source": "Source Name",
  "is_fabricated": false,
  "date": "2025-10-30"
}
```

## 🧪 Running Tests

```bash
pytest tests/
```

## 📊 What You'll Learn

- How to spot emotional manipulation in headlines
- Identifying vague vs. credible source citations
- Recognizing writing patterns in fabricated content
- Understanding source credibility indicators
- Developing systematic approaches to fact-checking

## 🎓 Educational Goals

This tool **augments human judgment** rather than replacing it. The goal is to:

1. **Sharpen pattern recognition** for common fabrication techniques
2. **Build systematic thinking** about source evaluation
3. **Practice critical analysis** in a safe, guided environment
4. **Understand limitations** of both human and automated detection

Remember: Critical thinking is a skill that improves with deliberate practice! 🧠💪
