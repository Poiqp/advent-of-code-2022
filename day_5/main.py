import re


input = 'test_data.txt'
input = 'real_data.txt'


def part_one(input):
    with open(input, 'r') as f:
        data = f.readlines()
        data = [x.replace('\n', '') for x in data]
        idx = data.index('')
        initial = data[:idx-1]
        orders = data[idx+1:]
        numbers = data[idx-1]

    state = [list() for y in range(int(numbers[-2]))]

    regex = r"(?:\[(\w)\]|\s\s\s\s)" 

    for line in reversed(initial):
        found = re.findall(regex,line)
        for k, element in enumerate(found):
            if element != '':
                state[k].append(element)

    regex = r"move (\d+) from (\d+) to (\d+)"

    for line in orders:
        found = re.findall(regex, line)[0]
        found = [int(x) for x in found]

        for move in range(found[0]):
            state[found[2]-1].append(state[found[1]-1].pop())

    result = []
    for letter in state:
        result.append(letter[-1])
    return ''.join(result)


def part_two(input):
    with open(input, 'r') as f:
        data = f.readlines()
        data = [x.replace('\n', '') for x in data]
        idx = data.index('')
        initial = data[:idx-1]
        orders = data[idx+1:]
        numbers = data[idx-1]

    state = [list() for y in range(int(numbers[-2]))]

    regex = r"(?:\[(\w)\]|\s\s\s\s)"

    for line in reversed(initial):
        found = re.findall(regex, line)
        for k, element in enumerate(found):
            if element != '':
                state[k].append(element)

    regex = r"move (\d+) from (\d+) to (\d+)"

    tmp = []
    for line in orders:
        found = re.findall(regex, line)[0]
        found = [int(x) for x in found]

        for move in range(found[0]):
            tmp.append(state[found[1]-1].pop())

        state[found[2]-1].extend(reversed(tmp))
        tmp = []

    result = []
    for letter in state:
        result.append(letter[-1])
    return ''.join(result)


print(part_one(input))
print(part_two(input))


































# def part_one(initial):

#     sum = 0
#     return sum



# def part_two(data):
#     sum = 0
#     return sum




# print(part_one(data))
# print(part_two(data))
