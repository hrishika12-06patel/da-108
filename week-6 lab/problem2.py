import os
import unicodedata
from collections import defaultdict

def detect_script(word):
    # Detect the script of a given word
    for char in word:
        script = unicodedata.name(char).split(' ')[0]
        if script.isalpha():  # Return the first script found
            return script
    return 'Unknown'

def main():
    # Load the text file
    file_path = 'file.txt'
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text into words
    words = text.split()

    # Count words per script
    script_counts = defaultdict(int)
    for word in words:
        script = detect_script(word)
        script_counts[script] += 1

    # Print a summary of the different languages/scripts present
    print("Summary of different scripts present in the text:")
    for script, count in script_counts.items():
        print(f"{script}: {count} words")

if __name__ == "__main__":
    main()