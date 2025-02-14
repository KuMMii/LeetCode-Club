class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        global R, C
        R, C= len(grid), len(grid[0])
        global visited 
        visited = [[False]*C for _ in range(R)]
        ans=0

        for r in range(R):
            for c in range(C):
                if not visited[r][c] and grid[r][c]=="1":
                    self.DFS(r, c, grid)
                    ans+=1

        return ans
    
    def DFS(self, r: int, c: int, grid: List[List[str]]):
        row=[-1, 1, 0, 0]
        col=[0,0,-1,1]

        visited[r][c]=True
        for i in range(4):
            nr, nc =r+row[i], c+col[i]
            if (0<=nr<R and 0<=nc<C) and not visited[nr][nc] and grid[nr][nc]=="1":
                self.DFS(nr, nc, grid)
