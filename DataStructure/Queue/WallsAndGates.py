"""
You are given a m x n 2D grid initialized with these three possible values:
    -1: A wall or an obstacle.
    0: A gate.
    INF: Infinity means an empty room.
We use the value 2^31 - 1 = 2147483647 to represent INF
as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate.
If it is impossible to reach a gate, it should be filled with INF.

EXAMPLE:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:
3  -1   0   1
2   2   1  -1
1  -1   2  -1
0  -1   3   4
"""

import numpy as np
from pprint import pprint


class Solution:

    def update_bfs_dist(self, graph, start, dist):
        queue = [start]
        visited = []

        # dist = {start: 0}

        i = 0
        while queue:
            print('--------------')
            print('level: ', i)
            v = queue.pop(0)
            print(queue)
            visited.append(v)
            i += 1
            for neighbor in graph[v]:
                # only add neighbor to queue if not visited, and not already in queue
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    row, col = neighbor
                    #if i < dist[row][col]:
                    dist[row][col] = i
            print(dist[0])
            print(dist[1])
            print(dist[2])
            print(dist[3])
        return dist

    def find_dist_to_gate(self, grid):
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(grid)
        cols = len(grid[0])
        m = rows + 2
        n = cols + 2
        # add walls around the given grid map
        # wrapped = [[-1]*n]*m  # this is does not work
        wrapped = [[-1 for i in range(n)] for j in range(m)]
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                wrapped[i][j] = grid[i - 1][j - 1]
                # print(i, j, wrapped[i][j])

        graph = {}
        gates = []
        rooms = []
        for i in range(rows):
            for j in range(cols):
                # when (i,j) is a gate
                if wrapped[i + 1][j + 1] == 0:
                    gates.append((i, j))
                # when (i,j) is a room or a gate
                if wrapped[i + 1][j + 1] != -1:
                    #print('------------------------')
                    #print((i, j), wrapped[i + 1][j + 1])
                    rooms.append((i, j))
                    neighbors = []
                    # check if the neighbor is a wall or not
                    if wrapped[i][j + 1] != -1:
                        neighbors.append((i - 1, j))
                    if wrapped[i + 2][j + 1] != -1:
                        neighbors.append((i + 1, j))
                    if wrapped[i + 1][j] != -1:
                        neighbors.append((i, j - 1))
                    if wrapped[i + 1][j + 2] != -1:
                        neighbors.append((i, j + 1))
                    graph[(i, j)] = neighbors
                    #print(neighbors)
        pprint(graph)

        # for gate in gates:
        #     print('---------------')
        #     print(gate)
        self.update_bfs_dist(graph, (0, 2), grid)


    def wallsAndGates_correct_solution(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # base case:
        if not rooms:
            return
        row, col = len(rooms), len(rooms[0])
        # find the index of a gate
        q = [(i, j) for i in range(row) for j in range(col) if rooms[i][j] == 0]
        for x, y in q:
            print('----------------------------------------')
            print(q)
            print(x,y)
            # get the distance from a gate
            distance = rooms[x][y]+1
            print("distance", distance)
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for dx, dy in directions:
                # find the INF around the gate
                new_x, new_y = x+dx, y+dy
                if 0 <= new_x < row and 0 <= new_y < col and rooms[new_x][new_y] == 2147483647:
                    # update the value
                    rooms[new_x][new_y] = distance
                    q.append((new_x, new_y))

            for i in range(row):
                print(rooms[i])

if __name__ == '__main__':
    eg1 = [[2147483647, -1, 0, 2147483647],
               [2147483647, 2147483647, 2147483647, -1],
               [2147483647, -1, 2147483647, -1],
               [0, -1, 2147483647, 2147483647]]
    print(eg1)
    sol = Solution()
    #sol.find_dist_to_gate(eg_grid)
    sol.wallsAndGates_correct_solution(eg1)
