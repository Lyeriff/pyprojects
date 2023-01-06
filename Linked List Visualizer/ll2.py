from manim import *
import numpy as np

#CONSTANTS
RADIUS, LINE_WIDTH, OPACITY, START_COORD = 0.3, 3, 0.3, -4

import csv
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


def line_pos(pos: list, inc: int =-1)->list:
    return [pos[0] - inc*RADIUS, pos[1], pos[2]]

L1 = LinkedList([1, 2, 3, 4, 5, 6, 7])
L2 = LinkedList([5,6,7,8], 2.5)
LL =[L1,L2]
L2.array[3].next = L1.array[4]

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

ptr_values = find_intersection(L2,L1)

class Video(MovingCameraScene):
    def construct(self):
        added = set()
        def update(mob):

            mob.become(Text(str(Node_Circle.node.val), 1 , 2, font_size=20, color=WHITE))

        obs=[]
        for L in LL:
            ptr = L.head
            
            while ptr and ptr not in added:

                added.add(ptr)
                Node_Circle=Circle(radius = RADIUS, color = WHITE).set_fill(YELLOW, opacity=OPACITY)
                Node_Circle.node = ptr
                if Node_Circle.node.next:
                    line = Arrow(start = line_pos(Node_Circle.node.position), 
                                end = line_pos(Node_Circle.node.next.position, 1), 
                                stroke_width=LINE_WIDTH)
                    print(f"from {Node_Circle.node.val} to {Node_Circle.node.next.val}")
                
                else: 
                    line = None
                    print(f"from {Node_Circle.node.val} to None")
                Node_Circle.line = line
                obs.append(Node_Circle)
                ptr=ptr.next
        
            for Node_Circle in obs:
                text = Text(str(Node_Circle.node.val), 1 , 2, font_size=20, color=WHITE)
                text.add_updater(update)

                Node_Circle.text = text
                self.add(Node_Circle)
                
                self.add(text)
                text.move_to(Node_Circle.node.position)
                Node_Circle.move_to(Node_Circle.node.position)
                print(Node_Circle.node.val, Node_Circle.node.position)
                if Node_Circle.line: 
                    self.add(Node_Circle.line)
                    self.wait(0.25)
            self.update_self(0)
            self.wait(1)
        
        ptr1 = Arrow(start=[START_COORD,1.5,0], end=[START_COORD,1,0])
        ptr1_name = Text("PTR-1", 1 , stroke_width=0.6, font_size=16, color=WHITE)
        self.add(ptr1)
        self.add(ptr1_name)

        ptr2 = Arrow(start=[START_COORD,2,0], end=[START_COORD,2.5,0])
        ptr2_name = Text("PTR-2", 1 , stroke_width=0.6, font_size=16, color=WHITE)
        self.add(ptr2)
        self.add(ptr2_name)
        for i, j in enumerate(ptr_values[0],ptr_values[1]):
            i_pos = i.position[:]
            i_pos[1]+=1
            ptr1.move_to(i_pos)
            ptr1_name.move_to([i_pos[0], i_pos[1]+1, i_pos[2]])
            j_pos = j.position[:]
            j_pos[1]+=1
            ptr2.move_to(j_pos)
            ptr2_name.move_to([j_pos[0], j_pos[1]+1, j_pos[2]])
            self.wait(0.8)

    

