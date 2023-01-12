import heapq
import sys

result=[]
n=int(sys.stdin.readline())
queue = []

for i in range (n):
    command=int(sys.stdin.readline())
    if (command==0):
        if(len(queue)==0):
            result.append(0)
        else:
            result.append(-heapq.heappop(queue))
    else:
        heapq.heappush(queue,-command)

for i in result:
    print(i)
