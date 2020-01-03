"""
Given a 2d grid map of ''1''s (land) and ''0''s (water),
count the number of islands. An island is surrounded by water
and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""


class Solution(object):

    def numIslands_mine(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num = 0
        if not grid:
            return num

        rows = len(grid)
        cols = len(grid[0])

        # visited = [[False for j in range(self.cols)] for i in range(self.rows)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    # iterative BFS
                    queue = [(i, j)]
                    while queue:
                        # print(queue)
                        x, y = queue.pop(0)
                        grid[x][y] = '0'
                        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                        for dx, dy in directions:
                            new_x, new_y = x + dx, y + dy
                            if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == '1':
                                # print((new_x, new_y))
                                queue.append((new_x, new_y))
                    num += 1

        print('total number of islands is ', num)
        return num

    def __init__(self, grid):
        self.rows = len(grid)
        self.cols = len(grid[0])

    def recursive_dfs(self, grid, x, y):
        if x < 0 or x >= self.rows or y < 0 or y >= self.cols or grid[x][y] == '0':
            return

        grid[x][y] = '0'
        self.recursive_dfs(grid, x + 1, y)
        self.recursive_dfs(grid, x - 1, y)
        self.recursive_dfs(grid, x, y + 1)
        self.recursive_dfs(grid, x, y - 1)

    def numIslands(self, grid):
        num = 0
        if not grid:
            return num

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.recursive_dfs(grid, i, j)
                    num += 1

        print('total number of islands is ', num)
        return num

if __name__ == '__main__':
    g1 = [['1', '1', '1', '1', '0'],
          ['1', '1', '0', '1', '0'],
          ['1', '1', '0', '0', '0'],
          ['0', '0', '0', '0', '0']]

    g2 = [['1', '1', '0', '0', '0'],
          ['1', '1', '0', '0', '0'],
          ['0', '0', '1', '0', '0'],
          ['0', '0', '0', '1', '1']]

    g3 = [['1', '1', '1', '1', '1'],
          ['1', '0', '0', '0', '1'],
          ['1', '0', '1', '0', '1'],
          ['1', '0', '0', '0', '1'],
          ['1', '1', '1', '1', '1']]

    g4 = [['1', '1', '0'],
          ['1', '0', '1'],
          ['0', '1', '1']]

    sol = Solution(g2)
    sol.numIslands_mine(g2)
