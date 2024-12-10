def main():
    book_text = get_file_contents("books/frankenstein.txt")
    print(book_text)

def get_file_contents(path):
    with open(path) as f:
        return f.read()

main()