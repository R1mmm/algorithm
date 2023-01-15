from collections import deque

n,k=map(int,input().split())
nlist = [i+1 for i in range(n)]
queue=deque(nlist)
result=[]

while(len(queue)>0):
    queue.rotate(-k)
    result.append(queue.pop())


print("<", end='')
print(', '.join(map(str,result)), end='')
print(">")