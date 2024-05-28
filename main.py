from io_ import input_, output_
import score
import info
import run
import load
import add_book
from uwords import uload
import sys
assert sys.version_info >= (3, 10)
while True:
    command_ = input_(":")
    match command_ :
        case "run":           
            run.run()
        case "start":
            run.run()
        case "score":
            output_("Erreichte Punktzahl:" + score.get_())
        case "info":
            info.info()
        case "exit":
            sys.exit()
        case "quit":
            sys.exit()
        case "load_book_list":
            output_(load.load("book_list"))
        case "add_book":
            #add_book.add_book()
            print("this function is not available in the current verion")
        case "unkown_words":
            book_name = input_("please enter book name:")
            uwords = uload(book_name)
            output_(uwords)
        case "uwords":
            book_name = input_("please enter book name:")
            uwords = uload(book_name)
            output_(uwords)
        case "load_books":
            #afserver.loadblist()
            print("this function is not available in the current verion")
        case _:
            output_("unkown command " + command_)
