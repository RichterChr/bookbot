def word_count(booktext):
    words = booktext.split()
    return len(words)

def character_count(booktext):
    character_dict = {}
    lowercase = booktext.lower()
    for letter in lowercase:
        if letter in character_dict:
            character_dict[letter] +=1
        else:
            character_dict[letter] = 1
    return character_dict


def sorted_list():
    print()