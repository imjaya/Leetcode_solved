#find the longest even length palindrome with str[i] and str[i+1] as mid point and update the maximumlength palindromic substring
def expand(str, low, high):
        length = len(str)
        while low >= 0 and high < length and str[low] == str[high]:
            low = low - 1
            high = high + 1      
        return str[low + 1:high]

class Solution:
      
    def longestPalindrome(self, s: str) -> str:
        max_str = ""
        max_length = 0
        for i in range(len(s)):
            # find a longest odd length palindrome with str[i] as mid point
            curr_str = expand(s, i, i)
            curr_length = len(curr_str)
            # update maximum length palindromic substring if odd length
            # palindrome has greater length
            if curr_length > max_length:
                max_length = curr_length
                max_str = curr_str
            # find a longest even length palindrome with str[i] and str[i+1] as mid points
            # Note that a even length palindrome has two mid points
            curr_str = expand(s, i, i + 1)
            curr_length = len(curr_str)
            # update maximum length palindromic substring if even length
            # palindrome has greater length
            if curr_length > max_length:
                max_length = curr_length
                max_str = curr_str
        return max_str
