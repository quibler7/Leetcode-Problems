class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # base case
        # function to perform dfs
        # calculate len or row and column
        # varibale count to return later
        # visited matrix to keep track of visited elements
        # traverse through grid if any element is 1 and not visited then incerement the count
        # and perform dfs on it.
        # lastly return the count.
        if not grid: return 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0" or visited[i][j]:
                return

            visited[i][j] = True

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        m, n = len(grid), len(grid[0])
        count = 0
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    dfs(i,j)
        return count
