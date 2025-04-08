def count_words_in_string(string):
    words_count = 0
    list_of_words = string.split()
    for word in list_of_words:
        words_count += 1
    return words_count

def count_characters_in_string(string):
    characters = {}
    for char in (string.lower()):
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters

def sort_on(dict):
    return dict["count"] 

def sort_dictionary(characters):
    sorted_characters = []


    for char in characters:
        single_character = {}
        single_character["char"] = char
        single_character["count"]=characters[char]
        sorted_characters.append(single_character)
    sorted_characters.sort(reverse=True, key=sort_on)

    return sorted_characters

