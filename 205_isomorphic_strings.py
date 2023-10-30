# Hashmap list approach TC: O(N), SC: O(N)
# This approach is based on the idea that the two given strings,
# if isomorphic, will in some way be exactly the same. If we have two
# isomorphic strings, we can replace the characters in the first string
# with the corresponding mapped characters to get the second string.
class Solution:
    def str_transform(self, input_str) -> str:
        first_pos = {}
        new_str = []
        for i, c in enumerate(input_str):
            if c not in first_pos:
                first_pos[c] = i
            new_str.append(str(first_pos[c]))
        return " ".join(new_str)

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.str_transform(s) == self.str_transform(t)