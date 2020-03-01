from functools import reduce

with open('input.txt') as f:
    data = f.read()

def parse_lines(data):
    packages = []
    for line in data.split('\n'):
        packages.append([int(dim) for dim in line.split('x')])
    return packages

def wrapping_paper(dims):
    return ((dims[0] * dims[1] + dims[1] * dims[2] + dims[0] * dims[2]) * 2) + (dims[0] * dims[1] * dims[2] / max(dims))

def ribbon(dims):
    return (sum(dims)-max(dims))*2 + reduce(lambda x, y: x * y, dims)

packages = parse_lines(data)

print(sum([wrapping_paper(dims) for dims in packages]))
print(sum([ribbon(dims) for dims in packages]))

        