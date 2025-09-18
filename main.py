from stats import *

def get_book_text(bookname):
    with open("books/"+bookname+".txt") as f:
        
        file_contents = f.read().replace('\n',' ').replace('    ', ' ').replace('   ', ' ').replace('  ', ' ')

    return file_contents

def main():
    l = create_dict_list(get_num_char(get_book_text("frankenstein")))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", get_num_words(get_book_text("frankenstein")), "total words")
    print("--------- Character Count -------")
    for d in l:
        print(d["char"]+":", d["num"])
    
main()