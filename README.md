# AI-PDF-Summarizer

This repository contains a Python application that uses the Pegasus model from the Hugging Face Transformers library to generate summaries of text extracted from PDF files. The application reads PDF files, extracts the text, and then uses the AI model to generate a concise summary. The summaries are then printed with a custom format. The project demonstrates the use of AI for natural language processing tasks such as text summarization.

## Requirements

- Python 3.9 or higher
- PyTorch
- Transformers
- SentencePiece
- pdfminer.six

## Installation

1. Clone the repository:

2. Navigate to the project directory:

```
cd AI-PDF-Summarizer
```

3. Install the required Python packages:

```
pip install -r requirements.txt
```

# Usage
1. Place your PDF files in the pdfs directory.
2. Run the main script:

```
python main.py
```

The script will read each PDF file, extract the text, generate a summary using the Pegasus model, and print the summary.

# License
This project is licensed under the terms of the MIT license.

Please replace the URL in the `git clone` command with the actual URL of your GitHub repository. Also, you might need to create a `requirements.txt` file that lists all the Python packages required for your project.
