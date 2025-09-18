import sys
from stats import *

def get_book_text(bookname):
    with open(bookname) as f:
        
        file_contents = f.read().replace('\n',' ').replace('    ', ' ').replace('   ', ' ').replace('  ', ' ')

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage Error")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bookpath = sys.argv[1]
        char_list = create_dict_list(get_num_char(get_book_text(bookpath)))
        print("============ BOOKBOT ============")
        print("Analyzing book found at", )
        print("----------- Word Count ----------")
        print("Found", get_num_words(get_book_text(bookpath)), "total words")
        print("--------- Character Count -------")
        for d in char_list:
            print(d["char"]+":", d["num"])
    
main()