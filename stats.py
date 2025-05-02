def sort_on(dict):
    return dict["num"]

def count_words_in_book(book_text):
    word_count = book_text.split()
    return len(word_count)

def count_char_occurances_in_book(book_text):
    char_tracker = {}
    for char in book_text:
        char = char.lower()
        if char in char_tracker:
            char_tracker[char] += 1
        else:
            char_tracker[char] = 1
    return char_tracker

def generate_sorted_char_count_report(char_dictionary):
    char_report_list = []
    
    for entry in char_dictionary:
        count = char_dictionary[entry]
        char_report_list.append({"char": entry, "num": count})
    
    char_report_list.sort(reverse=True, key=sort_on)
    return char_report_list
       