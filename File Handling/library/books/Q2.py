def add_book(book_list, book_id, title, author):
    book_list.append({"id": book_id, "title": title, "author": author, "available": True})

def display_books(book_list):
    for book in book_list:
        print(book)