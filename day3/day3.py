with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

fabric = [[0 for j in range(1000)] for i in range(1000)]
overlap_area = 0

for line in lines:
    tokens = line.split()
    x, y = (int(i) for i in tokens[2][:-1].split(','))
    width, height = (int(i) for i in tokens[3].split('x'))
    for column in range(x, x + width):
        for row in range(y, y + height):
            if fabric[column][row] == 1:
                fabric[column][row] = 'x'
                overlap_area += 1
            elif fabric[column][row] == 0:
                fabric[column][row] = 1

print(f'Part 1 => {overlap_area}')

for line in lines:
    tokens = line.split()
    identifier = tokens[0][1:]
    x, y = (int(i) for i in tokens[2][:-1].split(','))
    width, height = (int(i) for i in tokens[3].split('x'))
    overlap = False
    for column in range(x, x + width):
        for row in range(y, y + height):
            if fabric[column][row] == 'x':
                overlap = True
                break
        if overlap:
            break
    if not overlap:
        non_overlapping_id = identifier
        break

print(f'Part 2 => {non_overlapping_id}')
