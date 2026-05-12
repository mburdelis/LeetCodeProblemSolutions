class Solution:
    def dfs(self, grid: list[list[str]], i: int, j: int) -> None:
        # if out of bounds or if it's water, return
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            return
        # mark the current cell as visited
        grid[i][j] = "x"
        # visit all 4 neighbors
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1

        return count
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.numIslands([["1","1","1","1","0"],
                               ["1","1","0","1","0"],
                               ["1","1","0","0","0"],
                               ["0","0","0","0","0"]]))    # 1
    print(solution.numIslands([["1","1","0","0","0"],
                               ["1","1","0","0","0"],
                               ["0","0","1","0","0"],
                               ["0","0","0","1","1"]]))    # 3
