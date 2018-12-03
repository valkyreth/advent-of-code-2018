from itertools import cycle

with open('input.txt', 'r') as file:
    freqs = [int(i) for i in file.read().split('\n')]

# Part 1

total = sum(freqs)
print(f'Part 1 => {total}')

# Part 2

res, i = 0, 0
dup = set()

for i in cycle(freqs):
    res += i
    if res in dup:
        break
    dup.add(res)

print(f'Part 2 => {res}')
