def main():
    book_path = "books/frankenstein.txt"
    # open and very simply read in the entire file
    book_text = _get_file_contents(book_path)
    #count how many "words" there are, consider any space as a seperator of a word
    words = _count_words(book_text)
    #get a dict of all characters used and how many times
    #converted to lowercase, but keeping non-alpha chars
    char_dict = _count_letters(book_text)
    alpha = _only_letter_count(char_dict)
    alpha_sorted = dict(sorted(alpha.items(), key=lambda item: item[1], reverse=True))  #PLAYGROUND
    _print_report(book_path,words,alpha_sorted)


def _print_report(path,word_count,char_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for char in char_count:
        print(f"The '{char}' character was found {char_count[char]} times")
    print("--- End report ---")

def _get_file_contents(path):
    with open(path) as f:
        return f.read()

def _count_words(txt):
    tmp = txt.split()
    return len(tmp)

def _count_letters(txt):
    result = {}
    for char in txt:
        char = str(char).lower()
        if not (char in result):
            result[char] = 1
        else:
            result[char] += 1
    return result

def _only_letter_count(dict_in):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = {}
    for entry in dict_in:
        if entry in alphabet:
            result[entry] = dict_in[entry]
    return result
            

main()
exit()