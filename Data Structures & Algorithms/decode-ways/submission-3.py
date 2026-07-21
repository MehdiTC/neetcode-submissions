class Solution:
    def numDecodings(self, s: str) -> int:
        decMap ={}

        def dp(s):
            if s in decMap:  return decMap[s]
            if s == "": return 1
            if s[0] == "0": return 0

            if (len(s)>1 and s[0]=="1") or (len(s)>1 and s[0]=="2" and int(s[1])<=6):
                ans = dp(s[2:]) + dp(s[1:])
                decMap[s] = ans
                return ans
            else: 
                ans = dp(s[1:])
                return ans
        
        return dp(s)