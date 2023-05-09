from pathlib import Path
import re

valid_path = False

while not valid_path:
    book_path = input("Enter a valid relative path to a book:\n")
    if Path(book_path).exists():
        valid_path = True

path_to_file = Path(book_path)

with open(path_to_file) as f:
    file_contents = f.read()
    words = file_contents.split()

    def count_letters(file):
        letters = {}
        for char in file:
            regex = re.findall("[a-zA-Z]", char)
            try:
                if char == regex[0]:
                    if char.lower() in letters:
                        letters[char.lower()] += 1
                    else:
                        letters[char.lower()] = 1
            except:
                IndexError
        return letters

    print(f"\n\n--- Begin report of {path_to_file.name} ---")
    print(f"{len(words)} words found in the document")
    letter_counts = count_letters(file_contents)
    sorted_letters = sorted(letter_counts, key=letter_counts.get, reverse=True)
    for letter in sorted_letters:
        print(f"The '{letter}' character was found {letter_counts[letter]} times")
    print("--- End report ---")
