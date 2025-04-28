import sys
def get_book_text(book):
    with open(book) as f:
        book_contents = f.read()
        return book_contents
from stats import word_count
from stats import character_count
from stats import sort_characters
def main ():
    if len(sys.argv)!=2: #checks number of arguments
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) #exit with status code 1
    book_contents = get_book_text(sys.argv[1])
    count = word_count(book_contents)
    char_count = character_count(book_contents)
    char_list = sort_characters(book_contents)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + sys.argv[1])
    print("----------- Word Count ----------")
    print ("Found " + str(count) + " total words")
    print("--------- Character Count -------")
    for item in char_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()


        
