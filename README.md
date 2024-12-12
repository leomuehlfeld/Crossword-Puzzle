# Crossword Puzzle Generator

This project provides a Python script that generates a crossword-style grid of words from a `words.json` file. It arranges words horizontally and vertically, similar to a standard crossword puzzle, and outputs the results as SVG files. It also outputs a "key" where the placed words are highlighted. 

## Features
- **Custom Grid Size:** Specify grid dimensions (e.g., width, height).
- **Automatic Word Placement:** Reads from `words.json` and arranges words in a crossword-like layout.
- **SVG Output:** Produces `crossword_final.svg` and `crossword_key.svg`.

## Requirements
- Python 3.7 or later  
- Packages listed in `requirements.txt`

## Installation & Usage

```bash
# Clone the repository
git clone https://github.com/yourusername/crossword-generator.git
cd crossword-generator
```

# (Optional) Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

# Install required dependencies
```bash
pip install -r requirements.txt
```

# Prepare your word list in words.json (a JSON array of words)
```bash
Example: ["apple", "banana", "cherry", "date", "elderberry"]
```

# Run the script
```bash
python generate_words.py
```
