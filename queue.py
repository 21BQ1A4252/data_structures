import sys
from array import *
queue=array('i',[1,8])
def enqueue():
    ele=int(input())
    queue.append(ele)
    print(queue)
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print("deleted element",e)
def display():
    print("element")
    for i in queue:
        print(i)
while True:
    print("1.enqueue\n2.dequeue\n3.display\n4.exit")
    ch=int(input())
    if ch==1:
        enqueue()
        break
    elif ch==2:
        dequeue()
        break
    elif ch==3:
        display()
        break
    elif ch==4:
        sys.exit()
        break
    else:
        print("invalid choice")