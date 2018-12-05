import time

a = time.time()

with open('input.txt', 'r') as f:
    polymer = f.read()

polymer_copy = polymer

i = 0
while i < len(polymer) - 1:
    delete = False
    if (polymer[i].lower() == polymer[i + 1].lower()) and (
        (polymer[i].islower() and polymer[i + 1].isupper()) or
        (polymer[i].isupper() and polymer[i + 1].islower())):
        polymer = polymer.replace(polymer[i:i + 2], '')
        delete = True
        if i > 0:
            i -= 1
    if not delete:
        i += 1

shortest = len(polymer)

print(f'Part 1 => {shortest}')

for unit in set(polymer_copy.lower()):
    temp = polymer_copy.replace(unit, '').replace(unit.upper(), '')
    i = 0
    while i < len(temp) - 1:
        delete = False
        if (temp[i].lower() == temp[i + 1].lower()) and (
            (temp[i].islower() and temp[i + 1].isupper()) or
            (temp[i].isupper() and temp[i + 1].islower())):
            temp = temp.replace(temp[i:i + 2], '')
            delete = True
            if i > 0:
                i -= 1
        if not delete:
            i += 1
    if len(temp) < shortest:
        shortest = len(temp)

print(shortest)
print(time.time() - a)
