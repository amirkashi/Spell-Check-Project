
#Natural Language Processing Project

This project uesed probabilistic bigram language model and minimum edit distance (MED) to find the closest word given by user.

Data
For this project Penn tree-bank data (WSJ section 00-18) was used as to create a word list, unigram word occurance in the tree-bank data, and bigram words occurance in the tree-bank data. When user enter a word. 

Method
The code will find the closest word from the list using MED and language model.
In order to recommend the closed word to the user program will perform the following steps:

1- Check the word is in word list. If word is in the word list program will tell user that the entered word is correct.

2- If program find that the given word is not in the word list. It calculate MED and save words with 1 and 2 MED in a list. This is because 80% of errors are within 1 MED and almost all other errors are within 2 MED [1].

3- If program cannot find correct word with 1 or 2 MED it notifies the user and tell in what MED the correct word is found. Program will not recommend word with MED larger than 5.

4- Then program will use bigram language model to tell what word is the closest to the given word in 1 and 2 minimum edit distance. 


In the step 3 and 4 program finds probability of words with 1 and 2 or 3 to 5 MED. Then it find previous and next word of each recommended correct word. Finally, program finds probability of each correct words regarding to its previous and next word in each sentence of the training text. For example user give word “acress” to the program [this example obtained form the reference 1]. 
Program find that correct word could be “actress” or “across” using minimum edit distance.
Program sill find probability of “actress” given its previous and next word (n-1 and n+1, where n index number of actress in the sentence) lie following:
Probability of actress = P(actress|n-1) * P(n=1|actress) 
Then program will recommend correct word to the user regarding to this probability. 