import os

def main():
    path = construct_path()
    book_text = get_book_text(path)
    print(book_text)

def construct_path():
    script_dir = os.path.dirname(__file__)
    path_to_data = os.path.join("books", "frankenstein.txt")
    abs_file_path = os.path.join(script_dir, path_to_data)

    return abs_file_path

def get_book_text(abs_file_path):
    with open(abs_file_path) as f:
        return f.read()

main()