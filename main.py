def get_book_text():
    with open("./books/frankenstein.txt", "r") as file: # Opens file in read mode ("r"). If file doesn't exist, raises FileNotFoundError. May add >> encoding="utf-8" << if file contains non-ASCII characters. >><< added for highlighting only.
        return file.read()
    

def main():
    book_text = get_book_text()
    print(book_text)  # Print book to console

main()


# ALTERNATE VERSION:
# def main():
#     with open("./books/frankenstein.txt", "r") as file:
#         book_text = file.read()
#     print(book_text)      

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()