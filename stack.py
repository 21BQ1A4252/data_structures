import sys
from array import *
a=array("i",[])
while True:
    print("1.push\n2.pop\n3.Display\n4.exit")
    ch=int(input())
    if ch==1:
        ele=int(input())
        a.append(ele)
        print("inserted")
        print(a)
        break
    elif ch==2:
        if len(a)==0:
            print("array is empty")
        else:
            print("deleted element:",a.pop())
    elif ch==3:
        if len(a)==0:
            print("empty")
        else:
            for i in a:
                print(a)
    elif ch==4:
        sys.exit()
        break
    else:
        print("invalid choice")