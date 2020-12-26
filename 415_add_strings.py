class Solution(object):
    def addStrings(self, num1, num2):
        num_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,  '6':6, '7':7, '8':8, '9':9}
        # num3 = 0
        
        # Covert
        def str_to_int(num_str):

            num = 0

            for char in num_str:
                num = 10 * num + num_dict[char]

            return num
        

        num1 = str_to_int(num1)

        num2 = str_to_int(num2)

        # num3 = num1 + num2
        
        return str(num1 + num2)