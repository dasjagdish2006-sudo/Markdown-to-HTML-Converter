import os
import sys

try:
    import markdown
except ImportError:
    print("The 'markdown' package is not installed.")
    print("Run: pip install markdown")
    sys.exit(1)


def convert_markdown_to_html(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' not found.")
        return

    with open(input_file, "r", encoding="utf-8") as file:
        md_content = file.read()

    html_content = markdown.markdown(
        md_content,
        extensions=["extra", "codehilite", "tables"]
    )

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown to HTML</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
            line-height: 1.6;
            background: #f9f9f9;
            color: #222;
        }}
        pre {{
            background: #eee;
            padding: 12px;
            overflow-x: auto;
        }}
        code {{
            background: #f4f4f4;
            padding: 2px 5px;
            border-radius: 4px;
        }}
        blockquote {{
            border-left: 4px solid #ccc;
            padding-left: 12px;
            color: #666;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            border: 1px solid #ccc;
            padding: 8px;
            text-align: left;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(full_html)

    print(f"Conversion successful!")
    print(f"HTML file saved as: {output_file}")


def main():
    print("=== Markdown to HTML Converter ===")
    input_file = input("Enter markdown file name (e.g. input.md): ").strip()
    output_file = input("Enter output HTML file name (e.g. output.html): ").strip()

    if not output_file.endswith(".html"):
        output_file += ".html"

    convert_markdown_to_html(input_file, output_file)


if __name__ == "__main__":
    main()