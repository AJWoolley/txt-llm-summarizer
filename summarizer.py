"""
txt-llm-summarizer
------------------
Simple script that will take a .txt file, send its contents to an LLM API,
and write the summarized output to a new file.
"""

def summarize_file(input_path: str):
    """Placeholder function to simulate summarization."""
    output_path = input_path.replace(".txt", "_summary.txt")
    with open(input_path, "r") as infile, open(output_path, "w") as outfile:
        text = infile.read()
        summary = f"Summary placeholder for file: {input_path}\n\nOriginal length: {len(text)} characters."
        outfile.write(summary)
    print(f"Summary written to {output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python summarizer.py <input_file.txt>")
    else:
        summarize_file(sys.argv[1])

"""
To enable real LLM summarization:

1. Create an OpenAI account and generate an API key:
   https://platform.openai.com/account/api-keys

2. Set your key as an environment variable before running:
   export OPENAI_API_KEY="sk-..."

   (Windows PowerShell equivalent)
   setx OPENAI_API_KEY "sk-..."

3. Install the OpenAI Python SDK:
   python3 -m pip install --upgrade openai

The script will automatically use this key via the environment variable.
"""

