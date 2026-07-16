class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        count = 0
        text = ""
        seen=[]
        
        def backtrack(i,j):
            nonlocal count, text
            # check if inBound, matches the right letter, has been seen
            if count>len(word)-1 or i<0 or j<0 or i==len(board) or j==len(board[0]) or board[i][j]!=word[count] or (i,j) in seen:
                return 
            
            
            seen.append((i, j))
            count+=1
            text += board[i][j]
            if text==word:
                return True


            if backtrack(i-1, j): return True
            if backtrack(i+1, j): return True
            if backtrack(i,j+1): return True
            if backtrack(i,j-1): return True

            count-=1
            text = text[:count]
            seen.pop()

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if backtrack(i,j):
                        return True
        return False

            
        