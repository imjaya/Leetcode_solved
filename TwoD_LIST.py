#question
#2. <<Two Dimensional List>>
 #Write a function named "TwoD_LIST" that receives a positive integer n (n >= 1) as parameter and returns 
#a 2 dimensional list of numbers as shown below: 
#Notes:
#* The first list has 1 element, the second list has 2 elements, the third list has 3 elements and so on.
#* The first and the last element of each list are always 1.
#* The value of other elements in each list is the sum of the elements from the previous list with the same 
#  index and the index before. For example, the value of the element with index 2 in the list with 
#  index 5 is 10 which is equal to the sum of the values of the elements from previoius list with index 2 and index 1.
#* This is called Pascal's Triangle    

# function definition

def TwoD_LIST(number):
    n=int(number)  #inputin number
    final=[]       #initializing the final list
    for current_line in range(1, n + 1):  
        node_value = 1; #initializing current node value in a line
        line=[] 
        for i in range(1, current_line + 1):  
                           
            line.append(node_value)
            node_value = int(node_value * (current_line - i) / i);  
        final.append(line)
         
    return(final) #returning the final 2D list





def main():
    n=input("Enter the integer: ")
    pascal_Triangle=(TwoD_LIST(n))   #function call
    print("The returned 2D List is:")

    print(pascal_Triangle)
    
    print("Printing the list in Pascal Triangle form")
    for i in pascal_Triangle:
        print(i)
    
    

if __name__ == "__main__":
    main()