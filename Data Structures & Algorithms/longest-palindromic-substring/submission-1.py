class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        longestStr = ""
        
        def check(l, r):
            #print(f"s[l/r] is {s[l]} and l is {l} and r is {r} and l - r + 1 = {l - r + 1}")
            nonlocal longest, longestStr
            if r - l + 1 > longest: 
                longest = r - l + 1
                #print(s[l:r+1])
                longestStr = s[l:r+1]
            if l-1 >= 0 and r+1 < len(s) and s[l-1]==s[r+1]: 
                #print("yesss")
                check(l-1, r+1) 
                 
        for i in range(len(s)):
            check(i, i)
            if i+1<len(s) and s[i+1] == s[i]: check(i, i+1)
        #print(longest)
        return(longestStr)
