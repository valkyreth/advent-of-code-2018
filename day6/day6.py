import time

start = time.time()

with open('input.txt') as f:
    coords = {
        tuple(int(j) for j in i.split(',')): index + 1
        for index, i in enumerate(f.read().splitlines())
    }
    indices = {v: k for k, v in coords.items()}


begin_x = min(coords.keys())[0]
begin_y = min(coords.keys(), key=lambda x: x[1])[1]
end_x = max(coords.keys())[0]
end_y = max(coords.keys(), key=lambda x: x[1])[1]
max_manh = (end_x - begin_x) + (end_y - begin_y)

board = [[0 for x in range(begin_x, end_x + 1)]
         for y in range(begin_y, end_y + 1)]
count = {k: 0 for k in indices}
infinite = set()
special_region = 0

for y in range(begin_y, end_y + 1):
    for x in range(begin_x, end_x + 1):
        dist = 0
        min_d = max_manh
        
        for k, v in indices.items():
            manhattan = abs(x - v[0]) + abs(y - v[1])
            dist += manhattan
            if min_d == manhattan:
                rel_value = '.'
            elif manhattan < min_d:
                min_d = manhattan
                rel_value = k

        board[y - begin_y][x - begin_x] = rel_value

        if rel_value != '.':
            count[rel_value] += 1
            if not (begin_x < x < end_x and begin_y < y < end_y):
                infinite.add(rel_value)
        if dist < 10000:
            special_region += 1

for k in infinite:
    count.pop(k, None)

area = max(count.items(), key=lambda kv: kv[1])[1]

print(f'Part 1 => {area}')
print(f'Part 2 => {special_region}')

print(time.time() - start)
