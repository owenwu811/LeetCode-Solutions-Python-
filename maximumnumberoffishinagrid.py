


#correct solution using python3 using dfs:

#Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
#Output: 7
#Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            # Base case: if out of bounds or cell is zero (either water or already visited)
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] <= 0:
                return 0
            
            # Collect the fish in the current cell
            fish_count = grid[r][c]
            
            # Mark this cell as visited by setting it to 0 because we can't use the same cell twice aka catch the same fish twice 
            grid[r][c] = 0
            
            # Recursively explore the four directions
            fish_count += dfs(r + 1, c)
            fish_count += dfs(r - 1, c)
            fish_count += dfs(r, c + 1)
            fish_count += dfs(r, c - 1)
            
            return fish_count #we need to return fish_count because if we hit 0 looking in 4 directions, we can't continue down that path, and we want to know the max number of fish we can catch from this particular path and return it to the max_fish = max(max_fish, dfs(r, c))

        max_fish = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0:
                    # Perform DFS from each cell with fish and track the maximum fish count
                    max_fish = max(max_fish, dfs(r, c))
        
        return max_fish
