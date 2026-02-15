def main():
    book_text = get_book_text()
    return book_text  # Print book to console

def get_book_text():
    with open("./books/frankenstein.txt", "r") as file: # Opens file in read mode ("r"). If file doesn't exist, raises FileNotFoundError. May add >> encoding="utf-8" << if file contains non-ASCII characters. >><< added for highlighting only.
        return file.read()

def count_words():
    word_string = main()
    words = word_string.split()  # Split text into words based on whitespace
    word_count = len(words)  # Count the number of words
    # return f"Found {word_count} total words." # Return the number of words
    return word_count

def char_count():
    word_string = main()
    word_string.lower()  # Convert text to lowercase for case-insensitive counting
    char_count = {}
    for char in word_string:
        if char in char_count:
            char_count[char] += 1  # Increment count if character already exists in dictionary
        else:
            char_count[char] = 1  # Initialize count for new character
    return char_count

