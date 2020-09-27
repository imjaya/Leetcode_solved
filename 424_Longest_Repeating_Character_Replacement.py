class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = most = 0
        freq = {} # frequency table 
        for i in range(len(s)):
            freq[s[i]] = 1 + freq.get(s[i], 0)
            most = max(most, freq[s[i]])
            if ans < most + k: ans += 1
            else: freq[s[i - ans]] -= 1
        return ans


##sliding window
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = collections.defaultdict(int)
        max_lens = 0
        j = 0
        max_occur_freq = 0
        for i in range(len(s)):
            while j < len(s) and j - i - max_occur_freq <= k:
                freq[s[j]] += 1
                max_occur_freq = max(max_occur_freq, freq[s[j]])
                j += 1
            
            if j - i - max_occur_freq <= k:
                max_lens = max(max_lens, j - i)
            
            if freq[s[i]] == max_occur_freq:
                max_occur_freq - 1
            freq[s[i]] -= 1

        return max_lens