from stats import get_book_text
from stats import word_count
from stats import char_counter
from stats import sort_on
from stats import chars_to_sorted_list
import sys






def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
  
        text = get_book_text(sys.argv[1])
    
    num_count = word_count(text)
    cc = char_counter(text)
    print(f"Found {num_count} total words" )
   
    sort = chars_to_sorted_list(cc)
    for i in sort:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")

main()



