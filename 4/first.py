import numpy as np
import datetime

data = []
with open('./input.txt', 'r') as r_file:
    data = r_file.readlines()
    data = [ d.strip() for d in data ]

parsed_data = []
for row in data:
    parsed_data.append(
        {
            'time': datetime.datetime.strptime(row[1:17], '%Y-%m-%d %H:%M'),
            'message': row[19:]
        }
    )
parsed_data.sort(key=lambda r: r['time'])
data = parsed_data

guards = {}
cur_guard = -1
sleep_since = -1
for row in data:
    msg = row['message']
    time = row['time']
    if "Guard" in msg:
        id = msg[7:7+msg[7:].index(' ')]
        cur_guard = id
    elif 'falls' in msg:
        sleep_since = time.minute
    elif 'wakes' in msg:
        guards.setdefault(
            cur_guard, 
            [ 0 for _ in range(60) ]
        )
        for min in range(sleep_since, time.minute):
            guards[cur_guard][min]+=1

max_guard_id = max(guards, key=lambda id: sum(guards[id]))
guard_max_minute = np.argmax(guards[max_guard_id])
print(int(max_guard_id) * int(guard_max_minute))










