#!/bin/bash

# Usage: ./md_to_pdf.sh input_markdown.md output.pdf

INPUT_FILE="$1"
OUTPUT_FILE="$2"

if [ -z "$INPUT_FILE" ] || [ -z "$OUTPUT_FILE" ]; then
  echo "Usage: $0 input_markdown.md output.pdf"
  exit 1
fi

if ! command -v pandoc &> /dev/null; then
  echo "Error: pandoc is not installed. Please install it using your package manager."
  exit 2
fi

# Convert markdown to PDF using pandoc
pandoc "$INPUT_FILE" -o "$OUTPUT_FILE" --pdf-engine=xelatex --metadata title="Open House Party Report" --toc --highlight-style tango

echo "✅ Export complete: $OUTPUT_FILE"
