def main():
    book = "books/frankenstein.txt"
    book_text = get_book_text(book)
    total_words = count_words(book_text)
    print(f"Total words in the book: {total_words} words")

def get_book_text(path):
    with open(path, "r") as file:
        return file.read()
    
def count_words(book_text):
    words = book_text.split()
    return len(words)


main()
