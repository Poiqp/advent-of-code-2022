# with open('test_data.txt', 'r') as f:
#     data = f.readlines()
with open('real_data.txt', 'r') as f:
    data = f.readlines()


def part_one(data):
    data = [x.replace('\n','').split(' ') for x in data]

    elf = {
        'A' : 0,
        'B' : 1,
        'C' : 2
    }
    me = {
        'X' : 0,
        'Y' : 1,
        'Z' : 2
    }

    score_matrix = [
        [4,8,3],
        [1,5,9],
        [7,2,6]
    ]

    sum = 0
    for line in data:
        sum += score_matrix[elf[line[0]]][me[line[1]]]
    return sum


def part_two(data):
    data = [x.replace('\n','').split(' ') for x in data]

    elf = {
        'A' : 0,
        'B' : 1,
        'C' : 2
    }
    me = {
        'X' : 0,
        'Y' : 1,
        'Z' : 2
    }

    score_matrix = [
        [3,4,8],
        [1,5,9],
        [2,6,7]
    ]

    sum = 0
    for line in data:
        sum += score_matrix[elf[line[0]]][me[line[1]]]
    return sum

print(part_two(data))