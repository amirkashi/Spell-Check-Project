from collections import defaultdict


class Calculate_Unigram_Probability:    
    def calculate_unigram_probability(self, word_list):
        word_count = defaultdict(int)
        for words in word_list:
            word_count[words] += 1
        word_unigram_prob = {}
        for word in word_count:
            word_unigram_prob[word] = word_count[word] / float(len(word_count))
        return word_unigram_prob


class Calculate_Bigram_Probability:
    def calculate_bigram_probability(self, sentences):
        bigrams = defaultdict(int)
        for words in range(0, len(sentences) - 1):
            bigrams[(sentences[words], sentences[words + 1])] += 1
        bigram_probs = {}
        for items in bigrams:
            bigram_probs[items] = bigrams[items] / float(len(sentences))
        return bigram_probs
