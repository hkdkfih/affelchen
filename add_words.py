from io_ import input_, output_
def add_words():
    range_ = input_("please enter how many words the book have:")
    book_words = {}
    for i in range(int(range_)):
        word1 = input_("please enter word1 from word"+str(i+1)+":")
        word2 = input_("please enter word2 from word"+str(i+1)+":")
        book_words[word1] = word2
    return book_words