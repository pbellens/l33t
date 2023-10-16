'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

import typing


def neighbors(x: int, y: int, m: int, n: int):
    if x + 1 < m:
        yield (x+1, y)
    if y + 1 < n:
        yield (x, y+1)
    if x - 1 >= 0:
        yield (x-1, y)
    if y - 1 >= 0:
        yield (x, y-1)

def create_island(startx: int, starty: int, grid: typing.List[typing.List[int]]) -> typing.List[typing.Tuple[int, int]]:
    m = len(grid)
    n = len(grid[0])

    island = [(startx, starty)]
    visit = 0
    while visit < len(island):
        x, y = island[visit]
        for nx, ny in neighbors(x, y, m, n):
            if grid[nx][ny] == 1 and not (nx, ny) in island:
                island.append((nx, ny))
        visit += 1
    return island


def count_islands(grid: typing.List[typing.List[int]]) -> int:
    islands = []
    for i, r in enumerate(grid):
        for j, p in enumerate(r):
            if p == 1 and not any(((i,j) in island for island in islands)):
                islands.append(create_island(i, j, grid))
    return len(islands)
