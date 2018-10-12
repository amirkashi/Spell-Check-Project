from collections import defaultdict
import numpy 
from nltk.tokenize import sent_tokenize, word_tokenize
import string
from prettytable import PrettyTable


def read_file(input_file):
    read_Lines = [read_Lines.strip() for read_Lines in open(input_file) if "\t" in read_Lines]
    word_List = [word.split("\t")[0] for word in read_Lines if "\t" in word ]
    tags = [word.split("\t")[1] for word in read_Lines if "\t" in word ]
    return word_List, tags

def calculate_unigram_probability(word_list):
    word_count = defaultdict(int)
    for words in word_list:
        word_count[words] +=1
    
    word_unigram_prob = {}
    for word in word_count:
        word_unigram_prob[word] = word_count[word]/ float(len(word_count))
    
    return word_unigram_prob

def make_sentences(word_list):
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


if __name__ == '__main__':
    word_list, tags = read_file('wsj00-18_ss.tag')
    word_unigram_prob = calculate_unigram_probability(word_list)
    sentences = make_sentences(word_list)
    print (sentences)
