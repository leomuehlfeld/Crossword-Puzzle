# Crossword Puzzle Generator

This project provides a Python script that generates a crossword-style grid filled with words from a `words.json` file. The script arranges words horizontally and vertically, similar to a crossword puzzle. The final output is produced as scalable vector graphics (`.svg`) files, allowing you to view or print the resulting crossword.

## Features
- **Custom Grid Size:** Specify the desired dimensions of the grid (e.g., width and height).
- **Automatic Word Placement:** The script reads from a `words.json` file and attempts to arrange the words in a crossword-like configuration.
- **SVG Output:** Generates `crossword_final.svg` and `crossword_key.svg` for easy viewing, sharing, or printing.

## Requirements
- Python 3.7 or later
- Required Python packages (listed in `requirements.txt`)

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/crossword-generator.git
   cd crossword-generator```

2. **Create venv (optional)**
```bash 
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash 
pip3 install -r requirements.txt
``` 

Crossword Puzzle Generator

This project provides a Python script that generates a crossword-style grid filled with words from a words.json file. The script arranges words horizontally and vertically, similar to a crossword puzzle. The final output is produced as scalable vector graphics (.svg) files, allowing you to view or print the resulting crossword.

Features

Custom Grid Size: Specify the desired dimensions of the grid (e.g., width and height).
Automatic Word Placement: The script reads from a words.json file and attempts to arrange the words in a crossword-like configuration.
SVG Output: Generates crossword_final.svg and crossword_key.svg for easy viewing, sharing, or printing.
Requirements

Python 3.7 or later
Required Python packages (listed in requirements.txt)
Installation

Clone this repository:
git clone https://github.com/yourusername/crossword-generator.git
cd crossword-generator
Create and activate a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Usage

Prepare Your Word List:
Add or edit the words.json file with your desired words.
The words.json file should contain a JSON list of words. For example:
["apple", "banana", "cherry", "date", "elderberry"]
Run the Script:
python generate_words.py
By default, the script uses parameters defined within generate_words.py (such as grid size). You can edit the script to change the grid dimensions or other configuration parameters.
View the Output:
After running the script, you’ll find crossword_final.svg and crossword_key.svg in the project directory.
Open the .svg files in a browser or an SVG-compatible image viewer to see your crossword puzzle.
Customization

Grid Size:
Modify the corresponding variables (e.g., GRID_WIDTH, GRID_HEIGHT) in generate_words.py to adjust the puzzle size.
Word Filtering or Processing:
If needed, apply filters, checks, or transformations to the word list before placement within the script.
Output Format:
The script currently outputs .svg files. You can modify the script to generate additional output formats or integrate with other tools.
Troubleshooting

Words Not Fitting:
If the puzzle is not generated as expected, try reducing the number of words or increasing the grid size.
Overlapping or Missing Words:
Check your words.json for typos or duplicates. Adjusting the algorithm in generate_words.py may be necessary for more complex word sets.
License

This project is licensed under the MIT License. See the LICENSE file for details.

Contributing

Contributions are welcome! Feel free to open issues or submit pull requests with improvements, bug fixes, or new features.
