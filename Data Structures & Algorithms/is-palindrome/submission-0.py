class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(x.lower() for x in s if x.isalnum())
        for i, j in zip(clean_s, reversed(clean_s)):
            if i != j:
                return False
        return True