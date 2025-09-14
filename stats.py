def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def sort_on(item):
    
    return item["num"]

def chars_to_sorted_list(dict1):
    items = []
    for ch, n in dict1.items():
        items.append({"char": ch,"num": n})
        items.sort(key=sort_on, reverse=True)
    return items







def word_count(text):
    wc = 0
    for word in text.split():
        wc += 1
    return wc


def char_counter(text):
    t = text.lower()
    wc_dict = {}
    
    for wc in t:
        if wc not in wc_dict:
            wc_dict[wc] = 1
        else:
            wc_dict[wc] += 1
    return wc_dict
