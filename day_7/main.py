import re 
from typing import List


input = 'test_data.txt'
# input = 'real_data.txt'

with open(input, 'r') as f:
    data = f.readlines()
    data = [ x.replace('\n', '') for x in data ]


class Node():
    def __init__(self, name):
        self.parent = None
        self.children = []
        self.name = name 
        self.data = None 

    def add_child(self, child_name, child_data):
        child = Node(child_name)
        if child_data != None:
            child.data = int(child_data)
        else:
            child.data = child_data
        child.parent = self
        self.children.append(child)

    def next(self, child_name):
        for idx, child in enumerate(self.children):
            if (child.name == child_name):
                if child.data == None:
                    return self.children[idx]
        return self
    
    def prev(self):
        if self.parent != None:
            return self.parent
        else:
            return self

    def __repr__(self):
        rep_str = self.name + ' ' + str(self.data)
        for child in self.children:
            rep_str += f'\n  - {child.name} : {child.data}'
        return rep_str


def part_one(data):
    all_in_regex = r"(\$ ls)|(dir (\w+))|((\d+)\s(.*))|(\$\scd\s(\w+))|(\$\scd\s(\.\.))"
    curr_dir = Node('root')
    keep_root = curr_dir


    for line in data:
        found = re.search(all_in_regex, line)

        if found[7] and found[8]:
            # print('Going to child: ' + found[8])
            curr_dir = curr_dir.next(found[8])

        elif found[2] and found[3]:
            # print('Adding dir: ' + found[3])
            curr_dir.add_child(found[3], None)
        
        elif found[5] and found[6]:
            # print('Adding file: ' + found[6])
            curr_dir.add_child(found[6], found[5])

        elif found[9] and found[10]:
            # print('Reaching parent: ' + curr_dir.parent.name )
            curr_dir = curr_dir.prev()
        
    # print(keep_root)
    # print(keep_root.next('a'))
    # print(keep_root.next('d'))
    # print(keep_root.next('a').next('e'))

    def total_dir_size(node: Node, at_most: List) -> int:
        dir_size = 0
        for child in node.children:
            if child.data == None:
                dir_size += total_dir_size(child, at_most)[0]
            else:
                dir_size +=  child.data
        if dir_size <= 100000:
            at_most.append(dir_size)
        return dir_size, at_most


    total_size, at_most = total_dir_size(keep_root,at_most=[])

    return sum(at_most)


def part_two(data):
    all_in_regex = r"(\$ ls)|(dir (\w+))|((\d+)\s(.*))|(\$\scd\s(\w+))|(\$\scd\s(\.\.))"
    curr_dir = Node('root')
    keep_root = curr_dir

    for line in data:
        found = re.search(all_in_regex, line)

        if found[7] and found[8]:
            curr_dir = curr_dir.next(found[8])

        elif found[2] and found[3]:
            curr_dir.add_child(found[3], None)

        elif found[5] and found[6]:
            curr_dir.add_child(found[6], found[5])

        elif found[9] and found[10]:
            curr_dir = curr_dir.prev()

    def total_dir_size(node: Node, to_delete: List) -> int:
        dir_size = 0
        for child in node.children:
            if child.data == None:
                dir_size += total_dir_size(child, to_delete)[0]
            else:
                dir_size += child.data
        if dir_size >= 3636666:
            to_delete.append(dir_size)
        return dir_size, to_delete

    total_size, to_delete = total_dir_size(keep_root, to_delete=[])
    return min(to_delete)


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
