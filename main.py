from stats import get_num_words

def get_book_text(bookname):
    with open("books/"+bookname+".txt") as f:
        
        file_contents = f.read().replace('\n',' ').replace('    ', ' ').replace('   ', ' ').replace('  ', ' ')

    return file_contents

def main():
    print(get_num_words(get_book_text("frankenstein")), "words found in the document")
    
main()