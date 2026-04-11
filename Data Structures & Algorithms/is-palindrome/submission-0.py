class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        res = ""
        for ch in s:
            if ch.isalnum():
                res=res+ch.lower()
        
        return res == res[::-1]

        
        