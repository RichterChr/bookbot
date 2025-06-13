import sys

from stats import word_count, character_count, sorted_list, sort_on

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookpath = sys.argv[1]

    file_contents = get_book_text(bookpath)
    num_words = word_count(file_contents)
    chars_dict = character_count(file_contents)
    new_list = sorted_list(chars_dict)
    print_report(bookpath, num_words, new_list)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def print_report(bookpath, num_words, new_list):    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in new_list:
        char = letter["char"]
        num = letter["num"]
        print(f"{char}: {num}")

    print("============= END ===============")


main()
    