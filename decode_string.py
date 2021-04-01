class Solution:
    def decodeString(self, string: str) -> str:
        ## RC ##        
        ## APPROACH : 2 Stacks ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##

        nums = []
        strs = []
        num = ""
        s = ""
        for i, ch in enumerate(string):
            print(nums)
            print(strs)
            print(s)
            if ch.isdigit():
                num += ch
            elif ch == "[":
                nums.append(int(num))
                strs.append(s)
                num = ""
                s = ""
            elif ch == "]":
                s =  strs.pop() + s*nums.pop()       # watchout, replacing with the same string
            else:
                s += ch
        return s