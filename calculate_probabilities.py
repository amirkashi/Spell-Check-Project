from collections import defaultdict

class Calculate_Unigram_Probability:
    
    def calculate_unigram_probability(self, word_list):
        word_count = defaultdict(int)
        for words in word_list:
            word_count[words] +=1
        
        word_unigram_prob = {}
        for word in word_count:
            word_unigram_prob[word] = word_count[word]/ float(len(word_count))
        
        return word_unigram_prob
