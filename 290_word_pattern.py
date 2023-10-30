#Hashmap solution TC: O(len(pattern), len(s_list)) SC: O(num unique characters in pattern)
# hash map which keeps track of the first occurrences of each character in pattern and each word in s.
# As we go through each character-word pair, we insert unseen characters from pattern and unseen words from s.
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        if len(pattern) != len(s_list) or len(set(pattern)) != len(set(s_list)):
            return False

        pattern_map ={}
        for i in range(len(pattern)):
            p = pattern[i]
            s = s_list[i]
            if p not in pattern_map:
                pattern_map[p] = s
            elif pattern_map[p] != s:
                return False
            else:
                continue
        return True