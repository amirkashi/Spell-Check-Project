from nltk.tokenize import sent_tokenize, word_tokenize
import string
import read_file
from calculate_probabilities import *
from make_sentence import *
import find_unigram
import find_simple_bigram
import trigram
import find_bigram
import look_for_user_words
import string

class Spell_Check:
    def __init__(self):
        self.ROW_NUMBER_PRINT = 10 
        self.DEFAULT_MINIMUM_DISTANCE = 2
        self.word_list = None
        self.tag_list = None
        self.unigram_probability = None
        self.bigram_probability = None
        self.sentences = None
        self.trigram = None
        self.calculate_unigram_bigram_trigram_probability()

    def calculate_unigram_bigram_trigram_probability(self):
        print ("Please wait, training the model")
        read_data = read_file.read_file("./data/wsj00-18.tag")
        self.word_list, self.tag_list = read_data.make_wort_and_tag_lists()
        calculate_probabilities = Calculate_Unigram_Probability()
        self.unigram_probability = calculate_probabilities.calculate_unigram_probability(self.word_list)
        make_sentence = Make_Sentence_for_Training_Dataset()
        self.sentences = make_sentence.make_sentence(self.word_list, self.tag_list)
        calculate_probabilities = Calculate_Bigram_Probability()
        self.bigram_probability = calculate_probabilities.calculate_bigram_probability(self.sentences)
        find_trigrams = trigram.Trigram()
        self.trigram = find_trigrams.make_trigrams(self.sentences)

    def check_fist_word_capital(self, sentence):
        first_word_cap = True
        if sentence[0].islower():
            first_word_cap = False
        if first_word_cap == True:
            print ("First letter of the first word of the given sentence is capital.")
        else:
            print ("WARNING: First letter of the first word of the given sentence need to be capitalized.")

    def check_sentence_end_punctuation(self, sentence):
        punctuation = True
        if sentence[-1] not in string.punctuation:
            punctuation = False
        if punctuation == True:
            print ("Sentence ended with a punctuation.")
        else:
            print ("WARNING: Sentence need to be ended with a punctuation.")

    def get_user_sentence(self, input_sentence):
        if not input_sentence:
            print ("Sentence does not contain a word!")
        else:
            self.check_fist_word_capital(input_sentence)
            self.check_sentence_end_punctuation(input_sentence)
            user_input = input_sentence.strip()
            given_words = word_tokenize(user_input)
            looking_for_user_words = look_for_user_words.Look_For_User_Words()
            wrong_words = looking_for_user_words.find_wrong_words(given_words, self.unigram_probability)
            make_sentence_for_user = Make_Sentence_for_User_Input()
            user_sentence = make_sentence_for_user.make_sentence(given_words)
            print ("")
            if not wrong_words:
                print ("All word of the entered sentence are correct.")
            else:
                print ("Fowllowing word or words spelled incorectly:")
                for word in wrong_words:
                    print (word)
                for word in wrong_words:
                    find_unigrams = find_unigram.Find_Unigram()
                    find_unigrams.find_unigram(word, self.DEFAULT_MINIMUM_DISTANCE, self.unigram_probability, self.ROW_NUMBER_PRINT)
                    find_simple_bigrams = find_simple_bigram.Find_Simple_Bigram()
                    find_simple_bigrams.find_simple_bigram(word, self.DEFAULT_MINIMUM_DISTANCE, self.unigram_probability, self.ROW_NUMBER_PRINT, self.bigram_probability, self.trigram)
                    find_bigrams = find_bigram.Find_Bigram()
                    find_bigrams.find_bigram(user_sentence, word, self.DEFAULT_MINIMUM_DISTANCE, self.unigram_probability, self.bigram_probability, self.ROW_NUMBER_PRINT)
