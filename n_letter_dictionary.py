# Question
#3. <<N letter dictionary>>

#Write a function named n_letter_dictionary that receives a string (words separated by spaces) as parameter and 
#returns a dictionary whose keys are numbers and whose values are lists that contain unique words that have the number
# of letters equal to the keys. 

#Notes:
#* Each list of words with the same number of letters should be sorted in ascending order
#* The words in a list should be unique. For example, even though the word "them" is repeated twice in the above sentence, it is only considered once in the list of four letter words.
#* Capitalization does not matter, this means that all the words should be converted to lower case. For example the words "The" and "the" appear in the sentence but they are both considered as lower case "the".  

def n_letter_dictionary(input_string):
    input_string=input_string.lower()   #converting to lower case
    input_string=input_string.split()    # splitting words in a string
    input_string.sort()                 # sorting the string
    
    output_dictionary={}      
    for word in set(input_string):     
        index=len(word)        #identifying length of each word
        if index in output_dictionary:
            output_dictionary[index].add(word)
            (output_dictionary[index])
        else:
            output_dictionary[index] = {word}

    L=[]       # list to store only the keys
    L=sorted(output_dictionary)
    final_dictionary={}
    for i in L:
        final_dictionary[i]=list(sorted(output_dictionary[i]))
        
    return(final_dictionary)

def main():
    sentence="The way you see people is the way you treat them and the Way you treat them is what they become"
    count_dictionary={}
    count_dictionary=n_letter_dictionary(sentence)   #function call
    print(count_dictionary)
    
   
    
    

if __name__ == "__main__":
    main()