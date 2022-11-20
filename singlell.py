class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Single_ll:
    def __init__(self):
        self.head=None
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def delete_begin(self):
        if self.head is None:
            print("ll is empty")
        else:
            self.head=self.head.ref
    def delete_end(self):
        if self.head is None:
            print("ll is empty")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def print_ll(self):
        if self.head is None:
            print("ll is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
ll=Single_ll()
print("1.add begin\n2.add end\n3.delete begin\n4.delete end")
ch=int(input())
if ch==1:
    ll.add_begin(10)
    ll.add_begin(30)
    ll.print_ll()
elif ch==2:
    ll.add_end(60)
    ll.print_ll()
elif ch==3:
    ll.delete_begin()
    ll.print_ll()
elif ch==4:
    ll.delete_end()
    ll.print_ll()
else:
    print("invalid choice")