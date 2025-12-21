import sys
from stats import split_n_count, each_char_count, sorter


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    book = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    split_n_count(book)
    print("-------- Character Count --------")
    sorted = sorter(each_char_count(book))
    toggle = 0
    for chunk in sorted:
        for ignoring, using in chunk.items():
            if toggle > 0:
                print(*[f'{using}'], end="\n")
                toggle = 0
            elif toggle == 0:
                print(*[f'{using}:'], end=" ")
                toggle += 1
    print("============== END ==============")
        #print(chunk, end=" \n")
        #print(*[f'{v}' for k, v in chunk.items()])



main()