from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=[[] for _ in range(n+1)]
count=0
visited=[]
def bfs(num):
    global count
    queue=deque()
    for i in arr[num]:
        queue.append(i)

    if num in visited:
        return

    visited.append(num)
    count+=1

    while queue:
        num=queue.popleft()
        if num not in visited:
            visited.append(num)
        for i in arr[num]:
            if i not in queue and i not in visited:
                queue.append(i)

        

for i in range(m):
    u,v=map(int,input().split())  
    arr[u].append(v)
    arr[v].append(u)


for i in range(1,n+1):
    bfs(i)
print(count)