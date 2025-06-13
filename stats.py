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

def sort_on(dict):
    return dict["num"]


def sorted_list(chars_dict):
    sort_list = []
    for letters in chars_dict:
        if letters.isalpha():
            char = letters
            num = chars_dict[letters]
            new_dict = {"char" : char, "num": num}
            sort_list.append(new_dict)
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list