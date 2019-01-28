import numpy as np
import datetime

data = []
with open('./input.txt', 'r') as r_file:
    data = r_file.readlines()
    data = [ d.strip().split(',') for d in data ]
    tmp_data = []
    data = [ {'id': i+1, 'x': int(d[0].strip()), 'y': int(d[1].strip())} for i, d in enumerate(data) ]

grid = [
    [ {'ids': [],'dist': None } for _ in range(350) ] for _ in range(350)
]

def mark_len(row, x, y):
    dist = abs(row['x']-x) + abs(row['y']-y)
    if grid[x][y]['dist'] == None or dist < grid[x][y]['dist']:
        grid[x][y]['ids'] = [row['id']]
        grid[x][y]['dist'] = dist
    elif dist == grid[x][y]['dist']:
        grid[x][y]['ids'].append(row['id'])

for row in data:
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            mark_len(row, x, y)

inf_ids = []
np_grid = np.array(grid)
inf_ids += list(np_grid[0,:])
inf_ids += list(np_grid[-1,:])
inf_ids += list(np_grid[:,0])
inf_ids += list(np_grid[:,-1])
inf_ids = map(lambda i: i['ids'], inf_ids)
inf_ids = [item for sublist in inf_ids for item in sublist]
inf_ids = list(set(inf_ids))

# remove infs
for id in inf_ids:
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if id in grid[x][y]['ids']:
                grid[x][y]['ids'].remove(id)

closest_in_grid = [
    [ 0 for _ in range(350) ] for _ in range(350)
]

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if len(grid[x][y]['ids']) == 1:
            closest_in_grid[x][y] = grid[x][y]['ids'][0]

closest_in_grid = np.array(closest_in_grid)
unique_with_count = np.unique(closest_in_grid, return_counts=True)
u = unique_with_count[0]
c = unique_with_count[1]
if u[0] == 0:
    u = u[1:]
    c = c[1:]

print(unique_with_count)

sorted_c = list(c)
sorted_c.sort()
print(sorted_c)
print(max(sorted_c))

# id_counts = np.bincount(closest_in_grid.flatten())
# print(id_counts)
# print(np.argmax(id_counts))






