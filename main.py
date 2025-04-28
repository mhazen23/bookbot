def get_book_text(book):
    with open(book) as f:
        book_contents = f.read()
        return book_contents
from stats import word_count
from stats import character_count
from stats import sort_characters
def main ():
    book_contents = get_book_text("./books/frankenstein.txt")
    count = word_count(book_contents)
    char_count = character_count(book_contents)
    char_list = sort_characters(book_contents)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print ("Found " + str(count) + " total words")
    print("--------- Character Count -------")
    for item in char_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()



        
