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
