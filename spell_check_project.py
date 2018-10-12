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

def calculate_bigram_probability(sentences):
    bigrams = defaultdict(int)
    for words in range(0, len(sentences)-1):
        bigrams[(sentences[words], sentences[words+1])] +=1

    bigram_probs = {}
    for items in bigrams:
        bigram_probs[items] = bigrams[items] / float(len(sentences))
    
    return bigram_probs

def find_trigrams(sentences):
    trigram = defaultdict(int)
    for words in range(0, len(sentences)-2):
        trigram[(sentences[words], sentences[words+1], sentences[words+2])] += 1
    return trigram

def minimum_edit_distance(given_word, dictionary_word):
	med_matrix = numpy.zeros((len(given_word)+1 , len(dictionary_word)+1 ))

	for i in range(0, len(given_word)+1):
		med_matrix[i][0]=i
	for j in range(0, len(dictionary_word)+1):
		med_matrix[0][j]=j

	for i in range (1, len(given_word)+1):
		for j in range(1, len(dictionary_word)+1):
			if given_word[i-1]==dictionary_word[j-1]:
				med_matrix[i][j] = med_matrix[i-1][j-1] 
			else:
				med_matrix[i][j]= min(med_matrix[i][j-1], med_matrix[i-1][j], med_matrix[i-1][j-1])+1
	return med_matrix[i][j]

### --- working on given sentence --- ###
def check_fist_word_capital(sentence):
    first_word_cap = True
    if sentence[0].islower():
        first_word_cap = False
    #return first_word_cap
    if first_word_cap == True:
        print ("First letter of the first word of the given sentence is capital.")
    else:
        print ("WARNING: First letter of the first word of the given sentence need to be capitalized.")


def check_sentence_end_punctuation(sentence):
    punctuation = True
    if sentence[len(sentence)-1] not in string.punctuation:
        punctuation = False
    #return punctuation
    if punctuation == True:
        print ("Sentence ended with a punctuation.")
    else:
        print ("WARNING: Sentence need to be ended with a punctuation.")



if __name__ == '__main__':
    word_list, tags = read_file('wsj00-18_ss.tag')
    word_unigram_prob = calculate_unigram_probability(word_list)
    sentences = make_sentences(word_list)
    bigram_probs =  calculate_bigram_probability(sentences)
    trigram = find_trigrams(sentences)
    
    
