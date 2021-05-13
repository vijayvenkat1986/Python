import time


import sys
class outer:
    def __init__(self):
        print("Calling Constructor")
    def __del__(self):
        print("Calling Destructor")

t1 = outer()
t2=t1
t3=t1
t4=t1
print(sys.getrefcount(t1))



