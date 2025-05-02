# Imports
import sys
from stats import count_words_in_book
from stats import count_char_occurances_in_book
from stats import generate_sorted_char_count_report

# Logic
def get_book_text(file_path):
    with open(file_path) as book:
        book_text = book.read()
    return book_text
 
def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the book path from command line arguments
    book_content = get_book_text(sys.argv[1])
    word_count = count_words_in_book(book_content)
    char_occurances = count_char_occurances_in_book(book_content)
    print(f"{word_count} words found in the document.")
    #print(char_occurances)
    char_count_report = generate_sorted_char_count_report(char_occurances)
    
    print("""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------""")
    for entry in char_count_report:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()