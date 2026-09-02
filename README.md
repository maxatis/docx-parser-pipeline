# DOCX to Markdown Pipeline

A production-grade, fault-tolerant Python microservice designed to batch-convert Microsoft Word documents (`.docx`) into clean, semantic Markdown (`.md`).

This tool is specifically optimized for Data Ingestion pipelines, preparing complex documents (including tables and lists) for Large Language Models (LLMs), RAG architectures, and AI-driven data extraction.

## Features

* **High-Fidelity Parsing:** Powered by Microsoft's `markitdown` engine, ensuring accurate extraction of text, headers, and complex table structures.
* **Batch Processing:** Automatically scans and processes all `.docx` files in the input directory.
* **Secure & Local-Only:** Uses strictly local conversion to ensure the parser never attempts external network calls for embedded URIs, keeping your data secure.
* **Graceful Degradation:** Built-in fault tolerance. If one document is corrupted or contains invalid XML, the pipeline logs the stack trace and continues processing the remaining files.
* **Idempotent Infrastructure:** Automatically generates necessary directory structures (`input_docs/`, `output_md/`, `logs/`) upon the first run.
* **Code Quality:** Strictly typed (Mypy), linted (Ruff), and protected by pre-commit hooks and GitHub Actions.

## Project Structure

```text
.
├── input_docs/           # Drop your .docx files here
├── output_md/            # Converted .md files will appear here
├── logs/                 # Detailed execution logs (parser.log)
├── src/
│   ├── config.py         # Directory and path configurations
│   └── converter.py      # Core parsing logic
├── main.py               # Pipeline orchestrator
├── requirements.txt      # Production dependencies
└── Makefile              # Development commands abstraction
```

## Quick Start
### 1. Requirements
* Python 3.10 or higher.
### 2. Installation
Clone the repository and set up a virtual environment:
```Bash
git clone https://github.com/maxatis/docx-parser-pipeline.git
cd docx-parser-pipeline
python -m venv venv
```
Activate virtual environment
* **On macOS/Linux:**
```Bash
source venv/bin/activate
```
* **On Windows:**
```Bash
.\venv\Scripts\activate
```
Install dependencies:
```Bash
pip install -r requirements.txt
```
### 3. Usage
1. Place your `.docx` files into the `input_docs/` folder (the folder will be created automatically if you run the script once, or you can create it manually).
2. Run the pipeline:
```Bash
python main.py
```

3. Retrieve your semantic Markdown files from the `output_md/` folder. Check `logs/parser.log` for any warnings or processing errors.

### Development & Contributing
This project uses strict static analysis to maintain code quality.

* Setup Development Environment:
```Bash
pip install -r requirements-dev.txt
pre-commit install
```

* Run Quality Checks (Linting, Formatting, Typing):
```Bash
make check
```

_Note: GitHub Actions CI is configured to run these checks automatically on every push and pull request._

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
