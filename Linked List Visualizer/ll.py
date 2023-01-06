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
    def __init__(self, data: list) -> None:
        head = Node(data[0], START_COORD)
        ptr = head
        x_loc = START_COORD
        for i in data[1:]:
            x_loc += 1.5
            ptr.next = Node(i,x_loc)
            ptr = ptr.next
        self.head = head 
        
    def display(self)-> None:
        head = self.head
        while head:
            print(f"{head.val}:{head.position[0]}->",end="")
            head=head.next
        print("None")

def line_pos(pos: list, inc: int =-1)->list:
    return [pos[0] - inc*RADIUS, pos[1], pos[2]]

L = LinkedList([1,'A','B',4, 5, 'C', 'Z'])
ptr_list = [0,1,2,4,1,5,2]
ptr_name = "Pointer 1"
class Video(MovingCameraScene):
    def construct(self):
        obs=[]
        
        def update_position(ob,dt):
            ob.PENDULUM.update_object(dt)
            ob.move_to(ob.PENDULUM.position)
            ob.LINE.put_start_and_end_on([0,2,0], ob.PENDULUM.position)
        ptr = L.head
        
        while ptr:
            Node_Circle=Circle(radius = RADIUS, color = WHITE).set_fill(YELLOW, opacity=OPACITY)
            Node_Circle.node = ptr

            line = Arrow(start = line_pos(Node_Circle.node.position), 
                        end = line_pos(Node_Circle.node.next.position, 1) if Node_Circle.node.next 
                        else [0,0,0], stroke_width=LINE_WIDTH)
            
            if not Node_Circle.node.next: line = None
            Node_Circle.line = line
            obs.append(Node_Circle)
            ptr=ptr.next
        
        for Node_Circle in obs:

            self.add(Node_Circle)
            text = Text(str(Node_Circle.node.val), 1 , 2, font_size=20, color=WHITE)
            self.add(text)
            text.move_to(Node_Circle.node.position)
            Node_Circle.move_to(Node_Circle.node.position)
            if Node_Circle.line: 
                print(Node_Circle.node.val, Node_Circle.node.position)
                self.add(Node_Circle.line)
                self.wait(0.25)
        self.update_self(0)
        self.wait(1)
        
        pointer = Arrow(start=[START_COORD,2,0], end=[START_COORD,1,0])
        pointer_name = Text(ptr_name, 1 , stroke_width=0.6, font_size=16, color=WHITE)
        self.add(pointer)
        self.add(pointer_name)
        for i in ptr_list:
            pos = obs[i].node.position[:]
            pos[1]+=1
            pointer.move_to(pos)
            pointer_name.move_to([pos[0], pos[1]+1, pos[2]])
            self.wait(0.8)

    

