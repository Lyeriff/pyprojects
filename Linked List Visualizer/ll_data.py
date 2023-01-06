import csv
RADIUS, LINE_WIDTH, OPACITY, START_COORD = 0.3, 3, 0.3, -4

class Node:
    def __init__(self, val, x_position=0, next = None) -> None:
        self.val = val
        self.next = next
        self.position  = [x_position,0,0]


class LinkedList:
    def __init__(self, data: list, height: int =0) -> None:
        head = Node(data[0], START_COORD, height)
        ptr = head
        x_loc = START_COORD
        self.array = [head]
        for i in data[1:]:
            x_loc += 1.5
            ptr.position[1]=height
            ptr.next = Node(i,x_loc)
            self.array.append(head)
            ptr = ptr.next
        ptr.position[1]=height
        self.head = head
        
    def display(self)-> None:
        head = self.head
        while head:
            print(f"{head.val}:{head.position[0]}->",end="")
            head=head.next
        print("None")

class Pointer:
    def __init__(self, name : str, itrs: int) -> None:
        self.name = name
        self.positions = []



L1 = LinkedList([1, 2, 3, 4, 5, 6, 7])
L2 = LinkedList([5,6,7,8,9,10], 2.5)
LL =[L1,L2]

def find_intersection(L1:LinkedList, L2:LinkedList) -> list:
    ptr1, ptr2 = L1.head, L2.head
    res1 = []
    res2 = []
    while ptr1!=ptr2:
        res1.append(ptr1)
        res2.append(ptr2)
        ptr1=ptr1.next if ptr1.next else L1.head
        ptr2=ptr2.next if ptr2.next else L2.head
    return [res1,res2]


f = open('test_data.csv', 'w')
# generate_data(LinkedList([1,2,3,4,5,6]), csv.writer(f))
f.close()    