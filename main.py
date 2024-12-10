def main():
    book_text = get_file_contents("books/frankenstein.txt")
    words = count_words(book_text)
    chars_count = get_chars_count(book_text)
    print(chars_count)

def get_file_contents(path):
    with open(path) as f:
        return f.read()
    
def count_words(str):
    return len(str.split())

def get_chars_count(str):
    chars_count = {}
    for char in str:
        char = char.lower()
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1
    return chars_count

main()