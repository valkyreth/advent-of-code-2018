with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

lines = sorted(lines)
guards = {}
sleep_start = 0
sleep_end = 0

for line in lines:
    tokens = line.split()
    current_time = int(tokens[1][:-1].split(':')[1])
    if len(tokens) > 4:
        guard_id = int(tokens[3][1:])
        if guard_id not in guards:
            guards[guard_id] = {
                'time': 0,
                'minutes': {i: 0
                            for i in range(60)}
            }
    else:
        if tokens[2] == 'falls':
            sleep_start = current_time
        else:
            sleep_end = current_time
            guards[guard_id]['time'] += sleep_end - sleep_start
            for minute in range(sleep_start, sleep_end):
                guards[guard_id]['minutes'][minute] += 1

# Part 1

rel_id = max(guards.items(), key=lambda kv: kv[1]['time'])[0]
rel_minute = max(guards[rel_id]['minutes'].items(), key=lambda kv: kv[1])[0]

print(f'Part 1 => {rel_id * rel_minute}')

# Part 2

rel_id = max(
    guards.items(),
    key=lambda kv: max(kv[1]['minutes'].items(), key=lambda kv: kv[1])[1])[0]
rel_minute = max(guards[rel_id]['minutes'].items(), key=lambda kv: kv[1])[0]

print(f'Part 2 => {rel_id * rel_minute}')
