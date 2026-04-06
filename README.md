# HanziExtractor 🇨🇳

**HanziExtractor** is a lightweight Python utility designed to "purify" your text files. It surgically removes English
words, numbers, and special symbols, leaving behind only Chinese characters (Hanzi) and proper Chinese punctuation.

Whether you are cleaning up messy OCR results, preparing a dataset for Natural Language Processing (NLP), or just trying
to extract the "meat" of a bilingual document, HanziExtractor gets it done in seconds! 🚀

---

## ✨ Why use HanziExtractor?

Cleaning text manually is a total headache. This tool is built for three specific scenarios:

* **Data Pre-processing:** Training a Chinese AI model or building a dictionary? You need noise-free data. This script
  strips out the English "clutter" automatically.
* **Language Learning:** Take a bilingual article and instantly generate a "Chinese-only" version to test your reading
  comprehension. 📖
* **OCR Cleanup:** Optical Character Recognition often "hallucinates" random English characters or symbols in the
  margins. HanziExtractor filters those out, leaving you with clean, readable text.

---

## 🛠️ Getting Started

You don't need to install any complex, heavy-duty libraries. This script uses Python’s built-in `re` (regex) module for
maximum speed and zero dependencies.

### 1. Save the Script

Download `extract_chinese.py` and place it in the folder where your target `.txt` files are located.

### 2. Run the Extraction

Open your terminal or command prompt and run:

```bash
python extract_chinese.py your_document.txt
```

### 3. Check the Output

The generated new file will be in the same directory named your_document_chinese.txt. Your
original file remains untouched! ✅

---

## 🔍 How it Works

The script uses a sophisticated Unicode range filter to distinguish between "noise" and "content." It specifically
targets:

| Category         | Unicode Ranges Included | Description                |
|------------------|-------------------------|----------------------------| 
| Common Hanzi     | \u4e00 - \u9fff         | CJK Unified Ideographs     |
| Rare Characters  | \u3400 - \u4dbf         | Extension A                |
| Punctuation      | \u3000 - \u303f         | Full-width marks like 。、「」 |
| Full-width Forms | \uff00 - \uffef         | Includes ，！？               |

---

## 🤝 Contributing

This is an open-source project! If you have ideas for better regex patterns (like supporting Cantonese-specific
characters or filtering out specific ads), feel free to open an issue or submit a pull request.