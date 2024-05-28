from io_ import input_, output_
import score
import load
import uwords
def book(book_name):
    uwload = uwords.uload(book_name)
    if uwload == {"uwload":" "}:
        book_json_name = "book_" + book_name
        book_words = load.load(book_json_name)
        for i in range(len(book_words)):
            output_("using book: book")
            word1 = list(book_words)[i]
            output_("word1:" + word1)
            word2_user = input_("pleas enter word2:")
            unkown_words_ = {}
            try:
                word2_programm = book_words[word1]
                if word2_user == word2_programm:
                    output_("richtig")
                    score.add_(1)
               
                else:
                    output_("falsch\nrichtiges Wort:" + word2_programm)
                    unkown_words_[word1] = word2_programm
              
        
            except:
                output_("falsch")
                output_(book_words[word1])
            uwords.save(book_name, unkown_words_)
    else:
        book_words = uwords.uload(book_name)
        for i in range(len(book_words)):
            word1 = list(book_words)[i]
            unkown_words_ = {}
            kown_words = []
            if word1 == "uwload":
                output_("")
            else:
                output_("using book: book")
                word1 = list(book_words)[i]
                output_("word1:" + word1)
                word2_user = input_("pleas enter word2:")
                try:
                    word2_programm = book_words[word1]
                    if word2_user == word2_programm:
                        output_("richtig")
                        score.add_(1)
                        kown_words.append(word1)
               
                    else:
                        output_("falsch\nrichtiges Wort:" + word2_programm)
                        unkown_words_[word1] = word2_programm
              
        
                except:
                    output_("falsch")
                    output_(book_words[word1])
            uwords.save(book_name, unkown_words_, kown_words)
           
        
    output_("Ereichte Punktzahl:" + score.get_())
   