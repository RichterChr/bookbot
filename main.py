from stats import word_count, character_count

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    num_words = word_count(file_contents)
    chars_dict = character_count(file_contents)
    print(f"{num_words} words found in the document")
    print(chars_dict)



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


main()
    