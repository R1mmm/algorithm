
import heapq
import sys

result=[]

n=int(sys.stdin.readline())
queue=[]
for i in range(n):
    x=int(sys.stdin.readline())
    if (x==0):
        if(len(queue)==0):
            result.append(0)
        else:
            num=heapq.heappop(queue)[1]
            result.append(num)
    else:
        if(x<0): 
            heapq.heappush(queue,(-x,x)) #앞은 절대값 뒤는 실제값
        elif(x>0):
            heapq.heappush(queue,(x,x))


for i in result:
    print(i)