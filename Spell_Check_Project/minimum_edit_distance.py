import numpy 

class Minimum_Edit_Distance:
    def minimum_edit_distance(self, given_word, dictionary_word):
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
