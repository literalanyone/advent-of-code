with open('input.txt') as f:
    data = f.read()

def part_one(data):
    return data.count('(') - data.count(')')

def part_two(data):
    floor = 1
    idx = 0
    while floor != 0:
        floor = floor + 1 if data[idx] == '(' else floor - 1
        idx += 1
    return idx

print(part_one(data))
print(part_two(data))