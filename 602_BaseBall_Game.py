class Solution:
    def calPoints(self, ops: List[str]) -> int:
        z=[]
        for i in ops:
            if i!="C" and i!="+" and i!="D":
                z.append(int(i))
            if i=="+":
                z.append(int(z[-1])+int(z[-2]))
            elif i=="D":
                z.append(2*int(z[-1]))
            elif i=="C":
                z.pop()
        return sum(z)