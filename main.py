from stats import count_words_in_string
from stats import count_characters_in_string
from stats import sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if not(len(sys.argv) == 2):
        print("Usage: python3 main.py <path_to_book>")

    path_to_file = sys.argv[1]
    
    
    book_text = get_book_text(path_to_file)
    num_words=count_words_in_string(book_text)
    num_characters=count_characters_in_string(book_text)
    sorted_chars_by_count = sort_dictionary(num_characters)


    #print(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")    
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars_by_count:
        if char["char"].isalpha():
            print(f"{char['char']}: {char["count"]}")

main()