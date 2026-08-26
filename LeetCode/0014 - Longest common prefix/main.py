from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min(len(word) for word in strs)
        prefix = ""

        for i in range(min_length):
            char = strs[0][i]

            for word in strs[1:]:
                if word[i] != char:
                    return prefix

            prefix += char

        return prefix