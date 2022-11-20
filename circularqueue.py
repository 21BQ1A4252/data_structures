class Node:
    def __init__(self):
        self.data=None
        self.link=None
class Queue:
    def __init__(self):
        front=None
        rear=None
    def enqueue(q,value):
        temp=Node()
        temp.data=value
        if q.front==None:
            q.front=temp
        else:
            q.rear.link=temp
        q.rear=temp
        q.rear.link=q.front
    def dequeue(q):
        if q.front==None:
            print("queue is empty")
            return -999999
        value=None
        if q.front==q.rear:
            value=q.front.data
            q.front=None
            q.rear=None
    def display(q):
        temp=q.front
        print("elements in circular queue:")
        while temp.link!=q.front:
            print(temp.data)
            temp=temp.link
        print(temp.data)
q=Queue()
q.front=q.rear=None
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print(q.dequeue())
q.display()
        