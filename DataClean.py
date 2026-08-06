import gutenberg_cleaner
import re

BRACKET_PATTERN = re.compile(r'\[[^[\]]*\]')


def remove_brackets(text):
    while True:
        text, count = BRACKET_PATTERN.subn('', text)
        if count == 0:
            break
    return text 


def clean_gutenberg_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    text = remove_brackets(gutenberg_cleaner.simple_cleaner(text)).replace("_","")
    clean_lines = [line for line in text.splitlines() if line.strip()]
    text = "\n".join(clean_lines)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"")


