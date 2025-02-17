def main():
    path_to_file = "books/frankenstein.txt"
    book_text = _get_file_contents(path_to_file)
    # words = _count_words(book_text)
    char_dict = _count_letters(book_text)
    print(char_dict)

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

main()
exit()