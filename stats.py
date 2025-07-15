def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents





def count_words(file_contents):
    num_words = 0
    words = file_contents.split()
    return len(words)


def count_char(text):
    char_count = {}
    
    lower_char = text.lower()
    for char in lower_char:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        
    return char_count

def sort_on(items):
    def get_num(dictionary):
        return dictionary["num"]
    item_list = []
    
    
    for item in items:
        temp_dict = {}
        temp_dict["char"] = item
        temp_dict["num"] = items[item]
        item_list.append(temp_dict)
    
    
    item_list.sort(reverse=True, key=get_num)
        
    


    
    return item_list

