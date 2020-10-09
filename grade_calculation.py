
# Question

#1. <<Grade Calculation>>
#Write a function named grade_calculation that receives a file name 
#and returns a dictionary that tells whether a student in this course passed or failed based on the following criteria. 

#Each line of the file will have the format:

#name, q1, q2, q3, q4, q5, q6, a1, a2, a3, a4, midterm, final

#where: 
#* name is a string
#* q1 through q6 are quiz scores (integers)
#* a1 through a4 are assignment scores (integers values)
#* midterm is midterm score (integer)
#* final is final exam score (integer)

#Notes:
#Two of the lowest quizzes should be dropped and the average of the remaining four quizzes is worth 25% of the total grade.
#The lowest assignment score should be dropped and the average of the remaining three assignments is worth 25% of the total grade.
#Midterm and final exams are each 25% of the total grade.
#Calculate the total score of the student and if the total score is greater than or equal to 60 (totalscore >= 60) then the student has passed. 
#Notice that the keys (names) and the values (pass or fail) of the dictionary should be all lower cased with no spaces in any of them.




def grade_calculation(f_name):
    file_pointer = open(f_name, 'r')     #opening the file in read only format
    scores = file_pointer.readlines()   # appending each line to a list named scores
    #print(type(scores))
    result_dict={}  # intializing the result dictionary

    for line in scores:   #iterating through each student
        name, q1, q2, q3, q4, q5, q6, a1, a2, a3, a4, midterm, final =  line.split(',')
        q_avg=0 #initializing average quiz score to 0
        a_avg=0 #initializing average assignment score to 0
        total_score=0 #initializing total score to 0

        q=[int(q1),int(q2),int(q3),int(q4),int(q5),int(q6)]  #appending quiz scores together
        a=[int(a1),int(a2),int(a3),int(a4)] #appending assignment scores together 
        midterm=int(midterm)
        final=int(final)
        
        for _ in range(0,2): # removing two lowest quiz scores
            q.remove(min(q))  
        
        a.remove(min(a))  # removing one lowest assignment scores

        for i in range(0,len(q)):
            q_avg+=q[i]/len(q)       #taking average of quiz scores

        for i in range(0,len(a)):
            a_avg=a_avg + a[i]/len(a)  #taking average of assignment scores
        
        
        total_score = ((float(q_avg)*0.25)) + ((float(a_avg)*0.25)) + ((float(midterm)*0.25)) + ((float(final)*0.25))
        
        if total_score>=60.0:
            result='pass'
            result_dict[name]=result
        else:
            result='fail'
            result_dict[name]=result
    return result_dict

def main():
    A={}
    A=grade_calculation('score.txt')   #function call
    print(A) # pinting the returned dictionary

if __name__ == "__main__":
    main()