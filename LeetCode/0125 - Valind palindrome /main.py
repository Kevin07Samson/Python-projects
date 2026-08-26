class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""

        for letters in s:
            if letters.isalnum():
                new_s += letters
        if new_s == new_s[::-1]:
            return True
        else:
            return False
