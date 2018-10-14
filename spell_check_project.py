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
    if punctuation == True:
        print ("Sentence ended with a punctuation.")
    else:
        print ("WARNING: Sentence need to be ended with a punctuation.")


### ----- Checking if word is in our word list (word_unigram_prob) ----- #
def look_for_word_in_list(word):
    if word in word_unigram_prob:
        return True 
    else:
        return False

def look_for_word_in_list_massage(word):
    if word in word_unigram_prob:
        print (word + ": was found in dictionary so it spelled correctly")
        look_for_word_in_list(True)
    else:
        print (word + ": was not found in dictionary so it spelled incorrectly ***")
        look_for_word_in_list(False) 

### -- unigram 
def find_unigram(word, def_med):

    table = PrettyTable(['Suggested Word', 'Minimum Edit distance', "Probability"])

    corrct_word_med_1 = []
    corrct_word_med_2 = []
    corrct_word_med_3 = []
    for correct_words in word_unigram_prob:
        temp = []
        med = minimum_edit_distance(correct_words, word)
        if 0< med <= def_med:
            temp.append(correct_words)
            temp.append(int(med))
            temp.append(word_unigram_prob[correct_words])
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
        def_med +=1
        find_unigram(word, def_med)
    elif  6 <= def_med:
        print (" ")
        print ("There is not a suggested word for" + word + "in a  reasonable edit distance.")
        print ("Code does not look for words with 6 or more edit distance")
    else:
        print (" ")
        print ("Sugested words for " + word + " using unigram model are:")
        print (table)


def find_wrong_words(given_words):
    wrong_words = []
    for wrd in given_words:
        look_for_word_in_list_massage(wrd)
        if look_for_word_in_list(wrd) == False:
            wrong_words.append(wrd)    
    return wrong_words

def spell_check(input_sentence, row_number_print, default_med, word_unigram_prob):
    inp = input_sentence.strip()
    given_words = word_tokenize(inp)

    check_fist_word_capital(input_sentence)
    check_sentence_end_punctuation(input_sentence)
    print ("")
    
    wrong_words = find_wrong_words(given_words)

    if not wrong_words:
        print ("All word of the entered sentence are correct.")
    else:
        print ("Fowllowing word or words spelled incorectly:")
        for word in wrong_words:
            print (word)

        for word in wrong_words:
            find_unigram(word, default_med)
            

    


if __name__ == '__main__':
    print ("Please wait ")
    word_list, tags = read_file('wsj00-18_ss.tag')
    word_unigram_prob = calculate_unigram_probability(word_list)
    sentences = make_sentences(word_list)
    bigram_probs =  calculate_bigram_probability(sentences)
    trigram = find_trigrams(sentences)
    row_number_print = 10 # number of corect word code suggest to user
    default_med = 2
    #input_sentence = raw_input("Please Enter a Aentece: ")
    input_sentence = "this is a bok"
    
    spell_check(input_sentence, row_number_print, default_med, word_unigram_prob)
    
    
    
    
    
