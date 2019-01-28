import numpy as np
import datetime
import sys

data = []
with open('./input.txt', 'r') as r_file:
    data = r_file.readlines()
    data = [ d.strip().split(',') for d in data ]
    tmp_data = []
    data = [ {'id': i, 'x': int(d[0].strip()), 'y': int(d[1].strip())} for i, d in enumerate(data) ]

# x_max = -1
# y_max = -1
# for row in data:
#     if row['x'] > x_max:
#         x_max = row['x']
#     if row['y'] > y_max:
#         y_max = row['y']

# print(x_max)
# print(y_max)

# grid = [
#     [ {'ids': [],'dist': -1} for _ in range(350) ] for _ in range(350)
# ]

# def mark_distances(row, x, y, dist):
#     if x < 0 or x+1 > len(grid) or y < 0 or y+1 > len(grid[0])-1:
#         return
#     if row['id'] in grid[x][y]['ids']:
#         return
#     if dist < grid[x][y]['dist']:
#         grid[x][y]['ids'] = [row['id']]
#         grid[x][y]['dist'] = dist
#     elif dist == grid[x][y]['dist']:
#         grid[x][y]['ids'].append(row['id'])
#     mark_distances(row, x+1, y, dist+1)
#     mark_distances(row, x, y+1, dist+1)
#     mark_distances(row, x, y-1, dist+1)
#     mark_distances(row, x-1, y, dist+1)

#     mark_distances(row, x+1, y+1, dist+2)
#     mark_distances(row, x+1, y-1, dist+2)
#     mark_distances(row, x-1, y+1, dist+2)
#     mark_distances(row, x-1, y-1, dist+2)

# for row in data:
#     mark_distances(row, row['x'], row['y'], 0)


