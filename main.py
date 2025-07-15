import sys
from stats import count_words
from stats import get_book_text
from stats import count_char
from stats import sort_on


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = sys.argv[1]
    
    
    text = get_book_text(book)
    word_count = count_words(text)
    char_count = count_char(text)
    sort = sort_on(char_count)
    
    
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for dictionary in sort:
        char = dictionary["char"]
        if char.isalpha():
            count = dictionary["num"]
            print(f"{char}: {count}")
    print("============= END ===============")







main()




