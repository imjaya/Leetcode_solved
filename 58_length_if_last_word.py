#Start from end skip the initial space characters and start counting
# as soon as you reach a non-space character till you reach the next space charater.
# TC: O(N) SC: O(1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s = s.strip()
        # words = s.split(" ")
        # return len(words[-1])
        cur_index  = len(s)
        length = 0
        while cur_index > 0:
            cur_index -= 1
            if length > 0 and s[cur_index] == " ":
                return length
            if s[cur_index] != " ":
                length += 1
        return length



        