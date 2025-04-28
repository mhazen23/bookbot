def get_book_text(book):
    with open(book) as f:
        book_contents = f.read()
        return book_contents
from stats import word_count
from stats import character_count
def main ():
    book_contents = get_book_text("./books/frankenstein.txt")
    count = word_count(book_contents)
    char_count = character_count(book_contents)
    print (str(count) + " words found in the document")
    print (char_count)python3 main.py
main()



        
