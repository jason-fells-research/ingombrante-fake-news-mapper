# Copilot / AI agent instructions — ingombrante-fake-news-mapper

This is a Python-based fake news detection and critical thinking training tool. These instructions help AI agents understand the codebase structure and development workflow.

## Project Overview
**Goal**: Train critical thinking skills by identifying patterns that distinguish real vs. fabricated news.
**Architecture**: Modular Python components with Jupyter notebooks for interactive demos.

## Quick Start Workflow

1. **Environment Setup** (REQUIRED FIRST)
   ```bash
   python -m venv venv && source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Test the System**
   ```bash
   python demo.py              # Quick CLI demo
   pytest tests/               # Run unit tests
   jupyter notebook            # Start interactive demos
   ```

## Key Architecture Components

### Core Modules (`src/`)
- `data_loader.py` — Loads/validates news articles from JSON fixtures
- `pattern_analyzer.py` — Detects fabrication indicators (sensationalism, vague sources, credibility markers)
- `trainer.py` — Interactive training sessions with hints and scoring
- `visualizer.py` — Creates charts/graphs for pattern analysis

### Data Flow Pattern
```
JSON articles → DataLoader → PatternAnalyzer → Trainer/Visualizer
```

### Sample Data (`tests/fixtures/sample_articles.json`)
- Contains 5 curated articles (3 real, 2 fabricated)
- Required fields: `title`, `content`, `source`, `is_fabricated`, `date`
- Keep samples small (<500 words) for demo purposes

## Development Patterns

### Adding New Detection Features
1. **Extend `PatternAnalyzer`** with new pattern methods
2. **Update analysis result structure** to include new metrics
3. **Add visualization support** in `PatternVisualizer`
4. **Create tests** in `test_core.py` with known examples

### Interactive Demo Rules
- **Notebooks are the primary user interface** — optimize for education/exploration
- **Keep analyses explainable** — users should understand WHY something is flagged
- **Provide learning hints** — don't just score, teach the patterns

### Testing Strategy
```bash
pytest tests/test_core.py      # Unit tests for core logic
python demo.py                # Integration test via CLI
# Manual: Run notebooks top-to-bottom without errors
```

## Project-Specific Conventions

### Data Handling
- **No large datasets in repo** — use small, curated samples in `tests/fixtures/`
- **Real examples needed** — fabricated examples should feel obviously fake to experienced readers
- **Balanced samples** — roughly equal real/fake articles for training

### Code Style
- **Docstrings required** for all public methods — explain purpose and expected I/O
- **Type hints encouraged** — helps with data flow understanding
- **Educational comments** — explain detection logic, not just implementation

### Jupyter Notebook Patterns
- **Cell-by-cell progression** — each cell should work independently
- **Visual explanations** — charts should teach, not just display data
- **Interactive elements** — encourage users to modify parameters and re-run

## Critical Files to Reference

- `README.md` — User-facing setup and educational goals
- `requirements.txt` — Python dependencies (data science stack)
- `tests/fixtures/sample_articles.json` — Example articles with known truth values
- `notebooks/demo_walkthrough.ipynb` — Primary user entry point
- `demo.py` — CLI version for quick testing

## When Making Changes

1. **Preserve educational value** — this is a learning tool, not just a classifier
2. **Test with sample data** — changes should work on existing fixtures
3. **Update both CLI and notebook interfaces** — maintain feature parity
4. **Consider false positive/negative rates** — balance detection accuracy with explainability

## Extension Points

- Add new pattern detection algorithms in `PatternAnalyzer`
- Create domain-specific datasets (sports, politics, health news)
- Build web interface using Flask/FastAPI
- Add machine learning classifiers using scikit-learn
- Integrate with real news APIs for live analysis
