results = {
    0: True
}
cur = 0
with open('./input.txt', 'r') as r_file:
    data = r_file.readlines()
    data = [ int(d.strip()) for d in data ]
    while True:
        for d in data:
            cur += d
            if results.get(cur, False) == True:
                print(cur)
                exit(0)
            else:
                results[cur] = True
