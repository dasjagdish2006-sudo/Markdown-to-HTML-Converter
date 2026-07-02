# Markdown to HTML Converter

A simple Python script that converts a Markdown (`.md`) file into a styled, standalone HTML file.

## How It Works

1. Prompts the user for a Markdown input file and desired HTML output filename.
2. Reads the Markdown content and converts it to HTML using the `markdown` library (with `extra`, `codehilite`, and `tables` extensions).
3. Wraps the converted HTML in a full HTML document with built-in CSS styling (clean fonts, code blocks, tables, blockquotes).
4. Saves the result as a ready-to-view `.html` file.

## Requirements

- Python 3
- `markdown` package

Install with:
```bash
pip install markdown
```

## Usage

```bash
python Converter.py
```

You'll be prompted to enter:
- The Markdown file to convert (e.g., `input.md`)
- The output HTML filename (e.g., `output.html`) — `.html` is appended automatically if omitted

## Notes

- Supports Markdown extras like tables, fenced code blocks, and code syntax highlighting classes.
- The generated HTML includes basic responsive styling out of the box.
