import numpy as np

data = []
with open('./input.txt', 'r') as r_file:
    data = r_file.readlines()
    data = [ d.strip() for d in data ]


field = [
    [ 0 for _ in range(1000) ] for _ in range(1000)
]
for row in data:
    id = row[1:row.index('@')]
    id = int(id.strip())
    start = row[row.index('@')+1:row.index(':')].split(',')
    start = [ int(s.strip()) for s in start ]
    size = row[row.index(':')+1:].split('x')
    size = [ int(s.strip()) for s in size ]

    for x_i in range(size[0]):
        for y_i in range(size[1]):
            field[start[0]+x_i][start[1]+y_i]+=1

np_field = np.array(field)

print((np_field > 1).sum())






