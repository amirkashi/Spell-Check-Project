import minimum_edit_distance
from prettytable import PrettyTable


class Find_Simple_Bigram(minimum_edit_distance.Minimum_Edit_Distance):
    def find_simple_bigram(self, word, default_med, word_unigram_prob, row_number_print, bigram_probs, trigram):
        table = PrettyTable(['Suggested Word', 'Minimum Edit distance', "Probability"])
        corrct_word_med_1 = []
        corrct_word_med_2 = []
        corrct_word_med_3 = []
        for correct_words in word_unigram_prob:
            temp = []
            score = 0.0
            med = self.minimum_edit_distance(correct_words, word)
            if 0< med <= default_med:
                for wrd in trigram:
                    if wrd[1] == correct_words:
                        p1 = word_unigram_prob[wrd[1]] * bigram_probs.get((wrd[0], wrd[1]), 0.01)
                        p2 = word_unigram_prob[wrd[1]] * bigram_probs.get((wrd[1], wrd[2]), 0.01)
                        prob = p1 * p2
                        score += prob
                temp.append(correct_words)
                temp.append(int(med))
                temp.append(round(score*100, 5))
                if med == 1:
                    corrct_word_med_1.append(temp)
                elif med == 2:
                    corrct_word_med_2.append(temp)
                else:
                    corrct_word_med_3.append(temp)
        corrct_word_table_sorted = sorted(corrct_word_med_1,key=lambda l:l[2], reverse=True)
        corrct_word_med_2_sorted = sorted(corrct_word_med_2,key=lambda l:l[2], reverse=True)
        for lst in corrct_word_med_2_sorted:
            corrct_word_table_sorted.append(lst)
        corrct_word_med_3_sorted = sorted(corrct_word_med_3,key=lambda l:l[2], reverse=True)
        for lst in corrct_word_med_3_sorted:
            corrct_word_table_sorted.append(lst)
        row = 0
        for items in corrct_word_table_sorted:
            if row < row_number_print:
                table.add_row(items)
            row+=1
        table.align['Suggested Word'] = "l"
        table.align['Probability'] = "l"
        if len(corrct_word_table_sorted) == 0:
            default_med +=1
            self.find_simple_bigram(word, default_med, word_unigram_prob, row_number_print, bigram_probs, trigram)
        elif 6 <= default_med:
            print " "
            print "There is not a suggested word for" + word + "in a  reasonable edit distance."
            print "Code does not look for words with 6 or more edit distance" 
        else:
            print " "
            print "Sugested words for " + word + " using simple bigram model are:"
            print table 
