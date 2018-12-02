data = []
with open('./input.txt', 'r') as r_file:
    data = r_file.readlines()
    data = [ d.strip() for d in data ]

for i in range(len(data)):
    this = data[i]
    for other_i in range(len(data)):
        if other_i <= i:
            continue
        other = data[other_i]

        incorrect = 0
        for i in range(len(this)):
            if this[i] != other[i]:
                incorrect+=1
            if incorrect > 1:
                break
        
        if incorrect <= 1:
            print(this)
            print(other)
            print(incorrect)


        



