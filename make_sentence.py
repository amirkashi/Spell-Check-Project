class Make_Sentence_for_Training_Dataset:
    def make_sentence(self, word_list, tags):
        sentences = word_list
        sentences[0:0] = [('<s>')]
        tags[0:0] = [('<s>')]
        for items in range(0, len(sentences)):
            if tags[items] == '.':
                sentences[items+1:items+1] = [('</s>')]
                tags[items+1:items+1] = [('</s>')]
                sentences[items+2:items+2] = [('<s>')]
                tags[items+2:items+2] = [('<s>')]
                sentences.append(('</s>'))
        return sentences


class Make_Sentence_for_User_Input:
    def make_sentence(self, list_of_words):
        sentence = list_of_words
        sentence[0:0] = [('<s>')]
        sentence.append('</s>')
        return sentence
        