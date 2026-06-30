class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            if not s[left].isalnum():
                # ?

            elif not s[right].isalnum():
                # ?

            elif s[left].lower() != s[right].lower():
                return False

            else:
                # move both pointers

        return True