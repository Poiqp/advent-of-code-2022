import math 

input = 'test_data.txt'
# input = 'real_data.txt'

with open(input, 'r') as f:
    data = f.readlines()
    data = [x.replace('\n', '') for x in data]

class Pin:
    def __init__(self,x,y) -> None:
        self.x = x 
        self.y = y 
    
    def move(self, direction: str):
        match direction:
            case 'R':
                self.x += 1 
            case 'L':
                self.x -= 1
            case 'U':
                self.y += 1
            case 'D':
                self.y -= 1

    
class Rope:
    def __init__(self) -> None:
        self.head = Pin(0,0)
        self.tail = Pin(0,0)
        self.visited = []
    
    def is_close(self) -> bool:
        if math.sqrt((self.head.x - self.tail.x)**2 + (self.head.y - self.tail.y)**2) > 1:
            return False
        else:
            return True

    def move_and_follow(self, direction: str, steps: int ) -> None:
        for step in range(0, steps+1):
            self.head.move(direction)
            print("H:  " + str(self.head.x) + "  " + str(self.head.y) )
            print("T:  " + str(self.tail.x) + "  " + str(self.tail.y) )
            if not self.is_close():
                self.tail.move(direction)
                print("T:  " + str(self.tail.x) + "  " + str(self.tail.y) )




    
def part_one(data):
    rope = Rope()
    for line in data:
        print(line)
        rope.move_and_follow(line[0], int(line[2]))
    return 


def part_two(data):
    pass

print(part_one(data))
# print(part_two(data))


































# def part_one(initial):

#     sum = 0
#     return sum



# def part_two(data):
#     sum = 0
#     return sum




# print(part_one(data))
# print(part_two(data))
