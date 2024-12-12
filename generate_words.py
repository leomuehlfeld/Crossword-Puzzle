import random
import string
import svgwrite
import json

# Canvas dimensions in cm (as per your wall size)
CANVAS_WIDTH_CM = 611
CANVAS_HEIGHT_CM = 263

# Decide on cell size in cm (adjust as needed)
CELL_SIZE_CM = 5  # Each cell will be 5cm x 5cm

# Calculate grid dimensions based on canvas size and cell size
GRID_WIDTH = int(CANVAS_WIDTH_CM / CELL_SIZE_CM)
GRID_HEIGHT = int(CANVAS_HEIGHT_CM / CELL_SIZE_CM)

# Read words from JSON file
with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

# Extract words if JSON is a list of dictionaries
if isinstance(words, list) and isinstance(words[0], dict):
    word_list = []
    for entry in words:
        german_word = entry.get('German', '').strip()
        english_word = entry.get('English', '').strip()
        if german_word:
            word_list.append(german_word)
        if english_word:
            word_list.append(english_word)
    words = word_list

# Preprocess words: remove spaces and convert to uppercase
words = [word.replace(" ", "").upper() for word in words]

# Remove duplicates
words = list(set(words))

# Sort words by length (longest first) to improve placement
words.sort(key=lambda x: len(x), reverse=True)

# Initialize the grid
grid = [['' for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Initialize a grid to track which cells are part of placed words
word_grid = [[False for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Colors for placed words and random letters
PLACED_WORD_COLOR = 'blue'      # Color for placed words in the key
RANDOM_LETTER_COLOR = 'black'   # Color for random letters
ALL_LETTERS_COLOR = 'black'     # Color for all letters in the final version

def can_place_word(word, x, y, direction):
    if direction == 'H':
        if y + len(word) > GRID_WIDTH:
            return False
        # Check cells before and after the word
        if y > 0 and grid[x][y - 1] != '':
            return False
        if y + len(word) < GRID_WIDTH and grid[x][y + len(word)] != '':
            return False
        for i in range(len(word)):
            xi = x
            yi = y + i
            letter = word[i]
            grid_cell = grid[xi][yi]
            if grid_cell == '':
                # Check adjacent cells (up and down) for conflicts
                if xi > 0 and grid[xi - 1][yi] != '':
                    return False
                if xi < GRID_HEIGHT - 1 and grid[xi + 1][yi] != '':
                    return False
            elif grid_cell == letter:
                pass  # Letter matches, acceptable overlap
            else:
                return False
        return True
    else:  # direction == 'V'
        if x + len(word) > GRID_HEIGHT:
            return False
        # Check cells before and after the word
        if x > 0 and grid[x - 1][y] != '':
            return False
        if x + len(word) < GRID_HEIGHT and grid[x + len(word)][y] != '':
            return False
        for i in range(len(word)):
            xi = x + i
            yi = y
            letter = word[i]
            grid_cell = grid[xi][yi]
            if grid_cell == '':
                # Check adjacent cells (left and right) for conflicts
                if yi > 0 and grid[xi][yi - 1] != '':
                    return False
                if yi < GRID_WIDTH - 1 and grid[xi][yi + 1] != '':
                    return False
            elif grid_cell == letter:
                pass  # Letter matches, acceptable overlap
            else:
                return False
        return True

def place_word(word):
    placed = False
    positions = []
    # Collect all possible positions
    for direction in ['H', 'V']:
        if direction == 'H':
            for x in range(GRID_HEIGHT):
                for y in range(GRID_WIDTH - len(word) + 1):
                    if can_place_word(word, x, y, direction):
                        positions.append((x, y, direction))
        else:  # direction == 'V'
            for x in range(GRID_HEIGHT - len(word) + 1):
                for y in range(GRID_WIDTH):
                    if can_place_word(word, x, y, direction):
                        positions.append((x, y, direction))
    if positions:
        # Randomly select one of the possible positions
        x, y, direction = random.choice(positions)
        if direction == 'H':
            for i in range(len(word)):
                xi = x
                yi = y + i
                grid[xi][yi] = word[i]
                word_grid[xi][yi] = True  # Mark cell as part of a placed word
        else:
            for i in range(len(word)):
                xi = x + i
                yi = y
                grid[xi][yi] = word[i]
                word_grid[xi][yi] = True  # Mark cell as part of a placed word
        placed = True
    return placed

# Place words in the grid
unplaced_words = []
for word in words:
    if not place_word(word):
        unplaced_words.append(word)

# Log unplaced words
if unplaced_words:
    print(f"Could not place {len(unplaced_words)} words. See 'unplaced_words.txt' for details.")
    with open('unplaced_words.txt', 'w', encoding='utf-8') as f:
        for word in unplaced_words:
            f.write(word + '\n')

# Fill empty spaces with random letters
for x in range(GRID_HEIGHT):
    for y in range(GRID_WIDTH):
        if grid[x][y] == '':
            grid[x][y] = random.choice(string.ascii_uppercase)

# Export to SVG
def export_to_svg(grid, word_grid, cell_size=CELL_SIZE_CM * 10, filename='crossword.svg', color_words=True):
    # Multiply cell_size by 10 to convert cm to mm for SVG (since SVG uses mm)
    width = GRID_WIDTH * cell_size
    height = GRID_HEIGHT * cell_size
    dwg = svgwrite.Drawing(filename, size=(f"{width}mm", f"{height}mm"))
    font_size = cell_size * 0.7

    for x in range(GRID_HEIGHT):
        for y in range(GRID_WIDTH):
            letter = grid[x][y]
            # Draw cell
            # dwg.add(dwg.rect(
            #     insert=(y * cell_size, x * cell_size),
            #     size=(cell_size, cell_size),
            #     fill='white',
            #     stroke='black',
            #     stroke_width=1
            # ))
            # Determine color based on whether words should be colored
            if color_words and word_grid[x][y]:
                color = PLACED_WORD_COLOR
            else:
                color = ALL_LETTERS_COLOR
            # Add letter
            dwg.add(dwg.text(
                letter,
                insert=((y + 0.5) * cell_size, (x + 0.8) * cell_size),
                text_anchor="middle",
                font_size=font_size,
                font_family="Arial",
                fill=color
            ))
    dwg.save()

# Export the final version with all letters in black
export_to_svg(grid, word_grid, filename='crossword_final.svg', color_words=False)

# Export the key version with words colored
export_to_svg(grid, word_grid, filename='crossword_key.svg', color_words=True)
