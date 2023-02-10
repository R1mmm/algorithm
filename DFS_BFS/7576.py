import sys
from collections import deque
input=sys.stdin.readline

m,n=map(int,input().split())
arr=[]
for i in range(n):
    tmp=map(int,input().split())
    arr.append(list(tmp))

dx=[-1,1,0,0]
dy=[0,0,1,-1]
result=0
queue=deque()

for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            queue.append((i,j))

def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]==0:
                arr[nx][ny]=arr[x][y]+1
                queue.append((nx,ny))                

bfs()
for i in arr:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    
    result=max(result,max(i))


print(result-1)
    