def main():
    path_to_file = "books/frankenstein.txt"
    book_text = _get_file_contents(path_to_file)
    words = _count_words(book_text)
    print(words)

def _get_file_contents(path):
    with open(path) as f:
        return f.read()

def _count_words(txt):
    tmp = txt.split()
    return len(tmp)




main()
exit()