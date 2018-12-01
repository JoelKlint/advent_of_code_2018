data = []
with open('./input.txt', 'r') as r_file:
    data = r_file.readlines()
    data = [ int(d.strip()) for d in data ]

print(sum(data))

