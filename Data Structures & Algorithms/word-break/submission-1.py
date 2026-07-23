class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}

        def dfs(s):
            curr = ""
            if s in memo: return memo[s]
            if s == "": return True 
            for i in range(len(s)):
                curr += s[i]
                if curr in wordDict:
                    if dfs(s[i+1:]): return True 
            memo[s] = False
            return False
        return dfs(s)