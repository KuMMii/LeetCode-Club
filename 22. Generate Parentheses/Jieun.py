class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def DFS(l:int, r:int, n:int, st:str):
            if l==r==n:
                ans.append(st)
                return
            
            if l<n:
                DFS(l+1,r,n,st+'(')
            if l>r:
                DFS(l,r+1,n,st+')')

        DFS(0,0,n,'')
        return ans
