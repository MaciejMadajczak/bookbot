def get_book_text(filepath):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():
    path_to_file = "/books/frankenstein.txt"
    print(get_book_text(path_to_file))

main()