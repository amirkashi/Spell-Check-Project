from collections import defaultdict


class Trigram:
    trigram = defaultdict(int)
    def make_trigrams(self, sentences:
        for words in range(0, len(sentences) - 2):
            self.trigram[(sentences[words], sentences[words + 1], sentences[words + 2])] += 1
        return self.trigramd
