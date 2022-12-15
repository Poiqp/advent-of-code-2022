input = 'test_data.txt'
input = 'real_data.txt'

with open(input, 'r') as f:
    data = f.readline()


def part_one(data):
    for letter in range(4, len(data)):
        if len(set(data[letter-4:letter])) == 4:
            return letter


def part_two(data):
    for letter in range(14, len(data)):
        if len(set(data[letter-14:letter])) == 14:
            return letter


# print(part_one(data))
print(part_two(data))


































# def part_one(initial):

#     sum = 0
#     return sum



# def part_two(data):
#     sum = 0
#     return sum




# print(part_one(data))
# print(part_two(data))
