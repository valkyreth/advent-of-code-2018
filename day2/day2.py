with open('day2.txt', 'r') as file:
    lines = file.read().split('\n')

# Part 1

double, triple = 0, 0
for line in lines:
    d_check, t_check = False, False
    for letter in set(line):
        if not d_check and line.count(letter) == 2:
            double += 1
            d_check = True
        elif not t_check and line.count(letter) == 3:
            triple += 1
            t_check = True
        if d_check and t_check:
            break

checksum = double * triple
print(f'Part 1 => {checksum}')

# Part 2

check = False
for x in range(len(lines)):
    for y in range(x + 1, len(lines)):
        diff = 0
        ans = ''
        for i in range(len(lines[x])):
            if diff > 1:
                break
            if lines[x][i] != lines[y][i]:
                diff += 1
            else:
                ans += lines[x][i]
        else:
            check = True
            break
    if check:
        break

print(f'Part 2 => {ans}')
