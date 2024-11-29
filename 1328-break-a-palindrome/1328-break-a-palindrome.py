class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2:
            return ""
        palindrome = [char for char in palindrome]
        i, j = 0, len(palindrome) - 1
        while i < j:
            if palindrome[i] != "a":
                palindrome[i] = "a"
                break
            i += 1
            j -= 1
        else:
            palindrome[-1] = "b" if palindrome[-1] != "b" else "c"
            
        return "".join(palindrome)