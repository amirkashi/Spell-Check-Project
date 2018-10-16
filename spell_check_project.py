from collections import defaultdict
import numpy 
from nltk.tokenize import sent_tokenize, word_tokenize
import string
from prettytable import PrettyTable
import read_file
from calculate_probabilities import *
import make_sentence
import find_unigram
import find_simple_bigram
import trigram
import find_bigram

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



# ---
def find_wrong_words(given_words):
    wrong_words = []
    for wrd in given_words:
        look_for_word_in_list_massage(wrd)
        if look_for_word_in_list(wrd) == False:
            wrong_words.append(wrd)    
    return wrong_words

def spell_check(input_sentence, row_number_print, default_med, word_unigram_prob, bigram_probs, trigram):
    inp = input_sentence.strip()
    given_words = word_tokenize(inp)
    #user_sentence = make_sentence.Make_Sentence_for_User_Input()
    #user_sentence =  user_sentence.make_sentence(given_words)

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
            find_unigrams = find_unigram.Find_Unigram()
            find_unigrams.find_unigram(word, default_med, word_unigram_prob, row_number_print)
            
            find_simple_bigrams = find_simple_bigram.Find_Simple_Bigram()
            find_simple_bigrams.find_simple_bigram(word, default_med, word_unigram_prob, row_number_print, bigram_probs, trigram)
            
            #find_bigrams = find_bigram.Find_Bigram()
            #find_bigrams.find_bigram()

    


if __name__ == '__main__':
    print ("Please wait ")
    read_file = read_file.read_file('wsj00-18_ss.tag')
    word_list, tags = read_file.make_wort_and_tag_lists()
    
    calculate_unigram_probabilities = Calculate_Unigram_Probability()
    word_unigram_prob = calculate_unigram_probabilities.calculate_unigram_probability(word_list)
    
    make_sentence = make_sentence.Make_Sentence_for_Training_Dataset()
    sentences = make_sentence.make_sentence(word_list, tags)
    
    calculate_unigram_probabilities = Calculate_Bigram_Probability()
    bigram_probs =  calculate_unigram_probabilities.calculate_bigram_probability(sentences)
        
    
    find_trigrams = trigram.Trigram()
    trigram = find_trigrams.make_trigrams(sentences)
    row_number_print = 10 # number of corect word code suggest to user
    default_med = 2
    #input_sentence = raw_input("Please Enter a Aentece: ")
    input_sentence = "this is a bok"
    
    spell_check(input_sentence, row_number_print, default_med, word_unigram_prob, bigram_probs, trigram)
    
    
    
