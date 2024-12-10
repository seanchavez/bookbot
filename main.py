def main():
    book_text = get_file_contents("books/frankenstein.txt")
    print_report(book_text)

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

def make_list_of_dicts(dict):
    lst = []
    for k, v in dict.items():
        if k.isalpha():
            lst.append({k: v})
    return lst

def sort_on(dict):
    return list(dict.values())[0]


def print_report(txt):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(txt)} words found in the document\n")
    char_counts = make_list_of_dicts(get_chars_count(txt))
    char_counts.sort(reverse=True, key=sort_on)
    for dict in char_counts:
        char, count = list(dict.items())[0]
        print(f"The '{char}' character was found {count} times")
    print("---End report---")

main()