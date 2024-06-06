# 8. Dictionaries Exercise:
# Create a dictionary of book titles and their authors. Write a function to search for a book
# by its title and return the author's name.

def search_book_by_title(books_dict, title):
    if title in books_dict:
        return books_dict[title]
    else:
        return "Book not found"


books = {
    "The Great Gatsby": "F. Scott Fitzgerald",
    "To Kill a Mockingbird": "Harper Lee",
    "Pride and Prejudice": "Jane Austen",
    "Jane Eyre": "Charlotte Brontë"
}

print(search_book_by_title(books, "To Kill a Mockingbird"))
