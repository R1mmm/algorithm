import sys
from collections import deque
input=sys.stdin.readline

m,n,h=map(int,input().split())
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]
arr=[[] for i in range(h)]

for i in range(n*h):
    tomate=map(int,input().split())
    arr[int(i//n)].append(list(tomate))

result=0
queue=deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k]==1:
                queue.append((i,j,k))

def bfs():
    while queue:
        z,x,y=queue.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]

            if 0<=nx<n and 0<=ny<m and 0<=nz<h and arr[nz][nx][ny]==0:
                arr[nz][nx][ny]=arr[z][x][y]+1
                queue.append((nz,nx,ny))                

bfs()
for i in arr:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        
        result=max(result,max(j))


print(result-1)
    