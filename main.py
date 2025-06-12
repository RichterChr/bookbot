from stats import word_count
from stats import character_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    word_count(file_contents)
    character_count(file_contents)


main()
    