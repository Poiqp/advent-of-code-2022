

# with open('test_data.txt', 'r') as f:
#     data = f.readlines()
with open('real_data.txt', 'r') as f:
    data = f.readlines()

def part_one(data):
    data = [x.split('\n')[0] for x in data ]
    data.append('')

    max_calories = 0
    curr_elve = 0

    for food in data:
        if food != '':
            curr_elve += int(food)
        else:
            if curr_elve > max_calories:
                max_calories = curr_elve
            curr_elve = 0 
    return max_calories


def part_two(data):
    data = [x.split('\n')[0] for x in data ]
    data.append('')

    top_three = [0,1,2]
    curr_elve = 0

    for food in data:
        if food != '':
            curr_elve += int(food)
        else:
            min_element = min(top_three)
            if curr_elve > min_element:
                top_three.remove(min_element) 
                top_three.append(curr_elve)
            curr_elve = 0 

    result = 0
    for x in top_three:
        result = result + x
    return result 


# print(part_one(data))
print(part_two(data))



