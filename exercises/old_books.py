book_anny_wants = input()
books_checked = 0
book = ""
while book != book_anny_wants:
    book = input()
    if book == "No More Books":
        break
    books_checked += 1
if book == "No More Books":
    print("The book you search for is not here!")
    print(f"You checked {books_checked} books.")
else:
    books_checked -= 1
    print(f"You checked {books_checked} books and found it.")
