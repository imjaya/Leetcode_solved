def letterCombinations(self, digits: str) -> List[str]:
        
        self.dig2l = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4':['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        
        res, self.dig_length = [], len(digits)
  
        self.build_combos(res, digits)
        return res
        
    def build_combos(self, res, digits:str, combination = ''):
        
        if len(combination) == self.dig_length:
            if combination: res.append(combination)
            return
        
        for char in self.dig2l[digits[0]]:
            self.build_combos(res, digits[1:],combination + char)