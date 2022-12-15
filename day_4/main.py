import re


# with open('test_data.txt', 'r') as f:
#     data = f.readlines()
with open('real_data.txt', 'r') as f:
    data = f.readlines()

data = [x.replace('\n','') for x in data]
    

def check_full_overlap(beg_1, end_1, beg_2, end_2):
    if beg_1 <= beg_2 and end_1 >= end_2:
        return True
    else:
        return False


def part_one(data):
    sum = 0

    regex = r"(\d+)-(\d+),(\d+)-(\d+)"

    for line in data:

        x = re.search(regex,line)
        fully_contains = False 
        if check_full_overlap(int(x[1]), int(x[2]), int(x[3]), int(x[4])):
            fully_contains = True
        else:
            if check_full_overlap(int(x[3]), int(x[4]), int(x[1]), int(x[2])):
                fully_contains = True
        
        if fully_contains:
            sum += 1
    return sum



def part_two(data):
    sum = 0

    regex = r"(\d+)-(\d+),(\d+)-(\d+)"

    for line in data:

        x = re.search(regex, line)
        contains = False
        if max(int(x[1]), int(x[3])) <= min(int(x[2]), int(x[4])):
            contains = True

        if contains:
            sum += 1
    return sum




# print(part_one(data))
print(part_two(data))
