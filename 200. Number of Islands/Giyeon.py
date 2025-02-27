from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[0] * n for _ in range(m)]
        cnt = 0

        # bfs
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited[r][c] = 1
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while q:
                cur = q.popleft()
                for dr, dc in directions:
                    nr = cur[0] + dr
                    nc = cur[1] + dc

                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        if grid[nr][nc] == "1":
                            q.append((nr, nc))
                            visited[nr][nc] = 1

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and not visited[r][c]:
                    bfs(r, c)
                    cnt += 1

        return cnt