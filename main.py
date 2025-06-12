def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(booktext):
    words = booktext.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    word_count(file_contents)

main()
    