from stats import word_count, character_count, sorted_list, sort_on

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    file_contents = get_book_text("books/frankenstein.txt")
    num_words = word_count(file_contents)
    chars_dict = character_count(file_contents)
    new_list = sorted_list(chars_dict)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
   # print(chars_dict)
    new_list.sort(reverse=True, key=sort_on)
    for letter in new_list:
        char = letter["char"]
        num = letter["num"]
        print(f"{char}: {num}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


main()
    