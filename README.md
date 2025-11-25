# Resume Analyzer

AI-powered resume analysis tool that uses Ollama LLM to analyze resumes against job titles and provide scoring and insights.

## Features

- **Multi-format Support**: Analyze PDF and CSV resume files
- **Batch Processing**: Process multiple resumes simultaneously
- **AI-Powered Analysis**: Uses Llama3.2 model via Ollama for intelligent scoring
- **Web Interface**: User-friendly Gradio GUI
- **Command Line**: CLI for automated workflows

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd resume-analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install and setup Ollama:
```bash
# Install Ollama (visit https://ollama.ai for installation instructions)
ollama pull llama3.2:1b
```

## Usage

### Web Interface
```bash
python src/gui_app.py
```

### Command Line
```bash
python src/resume_analyzer.py
```

## Project Structure

```
resume-analyzer/
├── src/
│   ├── resume_analyzer.py    # Core analysis logic
│   └── gui_app.py           # Gradio web interface
├── tests/                   # Test files
├── docs/                    # Documentation
├── examples/               # Example files
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## How It Works

1. **Text Extraction**: Extracts text from PDF/CSV files
2. **AI Analysis**: Sends resume text and job title to Ollama LLM
3. **Scoring**: Returns 0-100 score based on:
   - Skills match
   - Experience relevance
   - Qualifications
4. **Results**: Provides concise explanation with score

## Requirements

- Python 3.8+
- Ollama with llama3.2:1b model
- Dependencies listed in requirements.txt

## License

MIT License