class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        groups = {}

        for word in strs:
            letters = list(word)
            letters.sort()
            key = "".join(letters)

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return list(groups.values())


