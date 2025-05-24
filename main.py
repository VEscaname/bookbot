from stats import get_num_words, count_characters, format_char_count
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    path = sys.argv[1]

    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    char_count = count_characters(book_text)
    report_char_count = format_char_count(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in report_char_count:
       if dict.get("char").isalpha():
           print(f"{dict['char']}: {dict['num']}")

main()
