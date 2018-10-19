
# Spell Checking Project #

This project used probabilistic language models and a minimum edit distance (MED) to find the closest word to the word given by the user. The program gets a sentence from the user and reviews it word by word. If the program finds a wrong word or words in a given sentence, it will suggests at least 10 correct words for each wrong word. 

## Data ##
For this project, the Penn tree-bank data (WSJ section 00-18) was used to create a word list.

## Method ##
The code will find the closest word from the word list using **Minimum Edit Distance (MED) ** and **statistical language model**.
**Minimum Edit Distance (MED)** shows a level of dissimilarity of two words. The larger difference, the larger dissimilarity.
This project uses the probability of a word occurrence in training data to find the following statistics:
**Unigram:** is the number of occurrence of a word in given document. 
**Bigram:** and **Trigram** are occurrence of two and three consecutive words in a sentence of a given document, respectively. 
The code first calculates the above statistics and then performs the following steps to find if there is any wrong word in the given sentence:
* Checks if the first word of a sentence is started with a capital character. 
* Checks if the sentence has punctuation at the end. 
* Looks for all words in a sentence to find if the words are in the training dataset (unigram). If a word does not appear in the dataset, then that word is considered as a wrong word. The program then follows these steps to recommend the closed words to the wrong word:
  * It calculates the MED between the wrong word and all of the words in the training dataset, and saves words with an MED of 1 and 2. MEDs of 1 and 2 are chosen because 80% of all errors are within 1 MED and almost all of the other 20% of errors are within 2 MED.
  * If the program cannot find the correct word within 1 or 2 MED, it notifies the user and tells in what MED the correct word is found. The program will not recommend a word with an MED larger than 5.
  * Then program uses **unigram**, **bigram**, and **trigram** statistics to find which found correct word has the largest possibility to be recommended for a wrong word.
