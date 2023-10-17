class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result_strs =[""] * numRows

        if numRows == 1:
            return s

        increase = True
        n = 1
        res = 0
        for i in s:
            result_strs[res] += i
            if res == 0:
                increase = True
            if res == numRows - 1:
                increase = False            
            if increase:
                res += 1
            else:
                res -= 1
            n += 1
        return "".join(result_strs)
