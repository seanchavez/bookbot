def main():
    book_text = get_file_contents("books/frankenstein.txt")
    words = count_words(book_text)
    print(count_words(book_text))

def get_file_contents(path):
    with open(path) as f:
        return f.read()
    
def count_words(str):
    return len(str.split())

main()