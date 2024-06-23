def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_number_words(text)
    char_counted = get_amount_of_times(text)
    print(text)
    print(count)
    print(char_counted)
    report_to_console(char_counted, book_path)
    


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_number_words(text):
    word_list = text.split()
    count = 0
    for word in word_list:
        count += 1
    return count

def get_amount_of_times(text):
    lowercase_text = text.lower()
    counted_dict = {}
    for char in lowercase_text:
        if char in counted_dict:
            counted_dict[char] += 1
        else:
            counted_dict[char] = 1
    return counted_dict




def report_to_console(report, book):
    print(f"--- Begin report of {book} ---")
    for entry in report:
        print(f"The {entry} character was found {report[entry]} times")
    print("--- End report ---")
    



if __name__ == '__main__':
    main()