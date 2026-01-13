#defining a function named match_words taking 1 parameter words
def match_words(words):
    #initialising a variable counter = 0 
    ctr=0
    #empty list to store the words that have same first and last character
    lst=[]
    #picking 1 by 1 word from the list of words
    for word in words:
    # we will check length of the word and proceed only if it has more than 1 characters (because we need atleast 2 character to compare first and last)    
    #word[0] refers to the first character and word [-1] refers to the last character. if they are both equal then : 
        if len(word) >1 and word[0] == word[-1]:
            #incrementig counter by 1
             ctr +=1
             #adding that word to the empty list we had
             lst.append(word)
    # inside the function printing which words have the same first and last character
    print("List of the words with first and last chracater same\n",lst )
    # when i will call the function match words, it will return the count of words that had same 1st and last character
    return ctr
# a variable count will store the value returned by the function match words
# since match words can take only 1 parameter , we need to pass the list of words as a LIST enclosing in []
count=match_words(["abc","cbc","xyz","4674","effe"])
#print the value stored in variable count so that i know how many words had same 1st and last character
print("number of words with first and last character same:",count)

