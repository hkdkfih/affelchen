from io_ import input_, output_
import json
import add_words 
def add_book():
    book_name = input_("please enter the book name:")
    book_words = add_words.add_words()
    book_json = json.dumps(book_words, indent=4)
    book_file_name = "book_" + book_name + ".json"
    with open(book_file_name, "w") as outfile:
        outfile.write(book_json)
    with open("book_list.json") as book_list:
        book_list_decoded = json.load(book_list)

    book_list_decoded[book_name] = book_name

    with open("book_list.json", 'w') as book_list:
        json.dump(book_list_decoded, book_list)
    

