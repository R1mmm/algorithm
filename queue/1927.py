from queue import PriorityQueue
import sys

result=[]
n=int(sys.stdin.readline())
queue = PriorityQueue()

for i in range (n):
    command=int(sys.stdin.readline())
    if (command==0):
        if(queue.empty()):
            result.append(0)
        else:
            result.append(queue.get())
    else:
        queue.put(command)

for i in result:
    print(i)
