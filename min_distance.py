"""
Title: Lavenshtein's version of minimum edit distance
Author: Percy Brown
ID: 40382022
Date: 28/01/2021
Reference: Pseudocode from Speech and Language Processing: 3rd edition draft- Page 25
"""
#IMPLEMENTATION
"""
The function takes two parameters: the source and target words.
The various costs: insertion, deletion and substitution are fixed as 1, 1 and 2 rspectively.
However, we assume there is no substitution cost for substiuting a letter for itself.
The minimum edit distance is returned.
"""
def min_edit_distance(source, target):
    n = len(source)             #length of source word
    m = len(target)             #length of target word

    source_plus_space = n+1    #length of source word with an empty string at the beginning
    target_plus_space = m+1    #length of target word with an empty string at the beginning

    # Operation costs
    deletion_cost = 1
    insertion_cost = 1
    substitution_cost = 2      # any substitution can be represented by one insertion and one deletion

    # Distance matrix D with initialization of zeros for all fields, hence the zeroth row and column is the distance from the empty string
    D = [[0 for i in range(target_plus_space)] for i in range(source_plus_space) ]

    # Initializing the base cases
    # With a source substring of length i but an empty target string, going from i characters to 0 requires i deletes.
    for i in range(1,source_plus_space):
        D[i][0] =  D[i-1][0] + deletion_cost
    
    # With a target substring of length j but an empty source string, going from 0 characters to j characters requires j inserts
    for j in range(1, target_plus_space):
        D[0][j] =  D[0][j-1] + insertion_cost

    # Recurrence relation
    
    for i in range(1,source_plus_space):
        for j in range(1, target_plus_space):
            # If the source and target characters are the same, we assume no substitution cost.
            # The minimum distance in that field is retrieved as the immediate upper left diagonal value.
            if(source[i-1] == target[j-1]):
                D[i][j] = D[i-1][j-1]
            else:
                # The value of D[i][j] is computed by taking the minimum of the three possible paths through the matrix
                D[i][j] = min(D[i-1][j] + deletion_cost,
                            D[i-1][j-1] + substitution_cost ,
                            D[i][j-1] + insertion_cost)

    # Printing the matrix table
    
    for i in D:
        for r in i:
            print(r, end = " ")
        print()
    
    print()
    print("Minimum edit distance between " + source + " and " + target + ": " + str(D[n][m]))   #minimum edit distance returned


"""
The main function tests our minimum edit distance algorithm with parameters: intention and execution as source and target respectively.
It prints the minimum edit distance (8) between the source and target, with confirmation from the textbook.
"""
def main():
    source = "intention"
    target = "execution"

    # Displaying the matrix and minimum edit distance
    min_edit_distance(source, target)
    

main()


