import os

PATH_TO_BOOKS = "books"
PATH_TO_FILE = "frankenstein.txt"

def main():
    path = construct_path()
    book_text = get_book_text(path)
    num_of_words = get_num_of_words(book_text)
    letters_count = get_chars_dict(book_text)
    
    form_a_book_report(num_of_words, letters_count)

def construct_path() -> str:
    script_dir = os.path.dirname(__file__)
    path_to_data = os.path.join(PATH_TO_BOOKS, PATH_TO_FILE)
    abs_file_path = os.path.join(script_dir, path_to_data)

    return abs_file_path

def get_book_text(abs_file_path: str) -> str:
    with open(abs_file_path) as f:
        return f.read()
    
def get_num_of_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_chars_dict(text: str) -> dict[str, str]:
    lowered_text = text.lower()
    letter_count_dict = {}

    for char in lowered_text:
        if char in letter_count_dict:
            letter_count_dict[char] += 1
        else:
            letter_count_dict[char] = 1
    
    return letter_count_dict

def form_a_book_report(num_of_words: int, letters_count: dict[str, str]):
    sorted_dic = dict(sorted(letters_count.items()))

    print(f"--- Begin report of {PATH_TO_BOOKS}/{PATH_TO_FILE} ---")
    print(f"{num_of_words} words found in the document\n")

    for k, v in sorted_dic.items():
        if not k.isalpha():
            continue
        print(f"The '{k}' character was found {v} times")

    print("--- End report ---")

main()