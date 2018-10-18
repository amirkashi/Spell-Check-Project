
# Spell Checking Project #

This project uesed probabilistic bigram language model and minimum edit distance (MED) to find the closest word given by user. The program get a sentence form user and then it looks it word by word. If progrm find wrong word or words in a given sentece, it will suggest 10 correct word for each of wrong words. 

## Data ##
For this project Penn tree-bank data (WSJ section 00-18) was used as to create a word list.

## Method ##
The code will find the closest word from the word list using **Minimum Edit Distance (MED)** and **statistical language model**.
**Minimum Edit Distance (MED)** shows level of dissimilarity of two words which means the larger difference the larger dissimilarity 
This project uses probability of word occurance in a traing data to find the following statistics:
**Unigram:** is number of ocuurance of a word in qiven document. 
**Bigram:** and **Trigram** are occurence of two and three consequtive words in a sentence of a given document. 
The code first calculate the above statistics and then performs following steps to find if there are wrong word in the given sentence:
* Check if first word of sentence is started with a capital character. 
* Sentence has puncuation at the end. 
* Looks for all words sentence to find if it is in the training dataset (unigram). If a word does not appear in the dataset it consider that word as a wrong word. and will follow these steps to recomend the closed words to it:
  * It calculate MED between the worng word and all words of the training dataset and save words with 1 and 2 MED. This is because 80% of errors are within 1 MED and almost all other errors are within 2 MED.
  * If program cannot find correct word with 1 or 2 MED it notifies the user and tell in what MED the correct word is found. Program will not recommend word with MED larger than 5.
  * Then program will use **unigram**, **bigram**, and **trigram** statistics to find which founded correct word has the largest posibility to be recomended for a wrong word.
