class Look_For_User_Words:
    def look_for_word_in_list(self, word, unigram_prob):
        if word in unigram_prob:
            return True
        else:
            return False
    
    def find_wrong_words(self, given_words, unigram_prob):
        wrong_words = []
        for word in given_words:
            if_word_found = self.look_for_word_in_list(word, unigram_prob)
            if if_word_found:
                print (word + ": was found in dictionary so it spelled correctly")
            else:
                print (word + ": was not found in dictionary so it spelled incorrectly")
                wrong_words.append(word)
        return wrong_words
