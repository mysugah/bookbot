from stats import split_n_count, each_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    #print(get_book_text("/root/bookbot/books/frankenstein.txt"))
    book = get_book_text("/root/bookbot/books/frankenstein.txt")
    split_n_count(book)
    each_char_count(book)


main()