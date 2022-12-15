with open('test_data.txt', 'r') as f:
    data = f.readlines()
with open('real_data.txt', 'r') as f:
    data = f.readlines()

def part_one(data):
    data = [x.replace('\n','') for x in data]
    sum = 0
    for line in data:
        half = int(len(line)/2)
        compartment_1 = line[:half]
        compartment_2 = line[half:]
        common = list(set(compartment_1).intersection(compartment_2))[0]
        if common.isupper():
            sum += ord(common)-38
        else:
            sum += ord(common)-96
    return sum


def part_two(data):
    data = [x.replace('\n', '') for x in data]
    sum = 0

    for i in range(2, len(data),3):
        first = data[i-2]
        second = data[i-1]
        third = data[i]
        common = list(set(first) & set(second) & set(third))[0]
        if common.isupper():
            sum += ord(common)-38
        else:
            sum += ord(common)-96
    return sum





# print(part_one(data))
print(part_two(data))
