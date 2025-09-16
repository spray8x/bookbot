def get_book_text(bookname):
    with open("books/"+bookname+".txt") as f:
        file_contents = f.read()
    return file_contents

def main():
    print(get_book_text("frankenstein"))
    
main()