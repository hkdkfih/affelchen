from io_ import input_, output_
import books as b
import load
import sys
def run():

    books = load.load("book_list")
    output_("books:")
    output_(books)
    book = input_("please choose book:" )
    try:
        book_choise = books[book]
    except:
        output_("is not a book")
    match book_choise:
        case "exit":
            sys.exit()
        case "home":
            import main
        case _:
            b.book(book_choise)