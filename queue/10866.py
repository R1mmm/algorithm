import sys
from collections import deque

queue=deque()

n=int(input())
result=[]

for i in range (n):
    command=sys.stdin.readline().split()
    if(len(command)>1):
        if(command[0]=="push_back"):
            queue.append(command[1])
        else:
            queue.appendleft(command[1])
    else:
        if(len(queue)>0):
            if(command[0]=="front"):
                result.append(queue[0])
            elif(command[0]=="back"):
                result.append(queue[-1])
            elif(command[0]=="pop_front"):
                result.append(queue.popleft())
            elif(command[0]=="pop_back"):
                result.append(queue.pop())
            elif(command[0]=="empty"):
                result.append(0)
            else:
                result.append(len(queue))
        else:
            if(command[0]=="empty"):
                result.append(1)
            elif(command[0]=="size"):
                result.append(len(queue))
            else:
                result.append(-1)

for i in result:
    print(i)

#2 1
# 1