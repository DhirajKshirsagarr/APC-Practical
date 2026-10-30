from books import operations as book_ops
from members import operations as member_ops
from transactions import operations as txn_ops

book_list = []
member_list = []

book_ops.add_book(book_list, "B1", "Python Basics", "Shiva")
book_ops.add_book(book_list, "B2", "Data Structures", "Varad")
member_ops.add_member(member_list, "M1", "Rehan")

book_ops.display_books(book_list)
member_ops.display_members(member_list)

txn_ops.issue_book(book_list, "B1")
book_ops.display_books(book_list)

txn_ops.return_book(book_list, "B1")
book_ops.display_books(book_list)