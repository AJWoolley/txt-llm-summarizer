# txt-llm-summarizer

A simple Python project that uses an LLM API to summarize `.txt` files and generate summaries.

## Usage
- `summarize <input>.txt` will generate a summary and save it to `<input>_summary.txt`.

## Installation
- Python 3.8+
- Required Python packages are listed in `requirements.txt`.

## Features
- Summarize text files up to a few MB in size.
- Provide key takeaways as a summary.

## Contributing
- Fork the repo, create a branch, and submit a pull request with your changes.

## Quickstart

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/txt-llm-summarizer.git
   cd txt-llm-summarizer
   ```

2. **Install dependencies**
   ```bash
   python3 -m pip install -r requirements.txt
   ```

3. **Set your OpenAI API key**
   ```bash
   export OPENAI_API_KEY="sk-your-key-here"
   ```
   *(Windows PowerShell equivalent:)*  
   ```powershell
   setx OPENAI_API_KEY "sk-your-key-here"
   ```

4. **Run the summarizer**
   ```bash
   python3 summarizer.py your_text_file.txt
   ```

The summarized text will be saved to a new file ending in `_summary.txt`.
