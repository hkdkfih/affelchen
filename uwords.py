import load
def save(book, unkown_words = {}, kown_words = []):
    try :
        words = load.load("book_unkown_words_"+book)
        words.update(unkown_words)
        for i in range(len(kown_words)):
            del words[kown_words[i]]
        load.save("book_unkown_words_"+book, words)
    except :
        load.save("book_unkown_words_"+book, {"uwload":" "})
        words = load.load("book_unkown_words_"+book)
        words.update(unkown_words)
        load.save("book_unkown_words_"+book, words)
def uload(book):
    try :
        words = load.load("book_unkown_words_"+book)
        return words
    except :
        load.save("book_unkown_words_"+book, {"uwload":" "})
        words = load.load("book_unkown_words_"+book)
        return words
        