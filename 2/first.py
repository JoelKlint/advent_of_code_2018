data = []
with open('./input.txt', 'r') as r_file:
    data = r_file.readlines()
    data = [ d.strip() for d in data ]

twos = 0
threes = 0

for row in data:
    found_2 = False
    found_3 = False
    for char in row:
        if found_2 == False and row.count(char) == 2:
            found_2 = True
            twos+=1
        if found_3 == False and row.count(char) == 3:
            found_3 = True
            threes+=1
        if found_2 and found_3:
            break

print(twos * threes)
        



