def issue_book(book_list, book_id):
    for book in book_list:
        if book["id"] == book_id:
            book["available"] = False
            print("Book issued")

def return_book(book_list, book_id):
    for book in book_list:
        if book["id"] == book_id:
            book["available"] = True
            print("Book returned")