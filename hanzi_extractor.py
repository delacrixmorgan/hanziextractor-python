#!/usr/bin/env python3
"""
Extract Chinese characters and punctuation from a TXT document,
removing all English words and non-Chinese content.

Usage:
    python extract_chinese.py <input.txt>

Output:
    <input>_chinese.txt in the same directory
"""

import sys
import os
import re

def extract_chinese(text: str) -> str:
    """Keep only Chinese characters, Chinese punctuation, and newlines."""
    # Pattern matches anything that is NOT:
    # - CJK Unified Ideographs: \u4e00-\u9fff
    # - CJK Unified Ideographs Extension A: \u3400-\u4dbf
    # - CJK Compatibility Ideographs: \uf900-\ufaff
    # - CJK General Punctuation: \u3000-\u303f (includes 。、「」etc.)
    # - Fullwidth punctuation/forms: \uff00-\uffef (includes ，！？etc.)
    # - Newlines
    pattern = re.compile(
        r'[^\u4e00-\u9fff'
        r'\u3400-\u4dbf'
        r'\uf900-\ufaff'
        r'\u3000-\u303f'
        r'\uff00-\uffef'
        r'\n]+'
    )
    result = pattern.sub('', text)
    # Collapse multiple blank lines into one
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result.strip()


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {os.path.basename(__file__)} <input.txt>")
        sys.exit(1)

    input_path = sys.argv[1]

    if not os.path.isfile(input_path):
        print(f"Error: File not found: {input_path}")
        sys.exit(1)

    # Read the TXT file directly
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Fallback for files that might be encoded in GBK (common for older Chinese TXT files)
        with open(input_path, 'r', encoding='gbk', errors='ignore') as f:
            content = f.read()

    # Extract Chinese content
    chinese_text = extract_chinese(content)

    if not chinese_text:
        print("No Chinese characters found in the document.")
        sys.exit(0)

    # Build output filename
    base, _ = os.path.splitext(input_path)
    output_path = f"{base}_chinese.txt"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(chinese_text)

    print(f"Done! Chinese text saved to: {output_path}")
    print(f"Extracted {len(chinese_text)} characters.")


if __name__ == '__main__':
    main()