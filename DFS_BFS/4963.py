import sys
from collections import deque

input=sys.stdin.readline

dx=[-1,1,-1,1,0,0,1,-1]
dy=[-1,1,0,0,-1,1,-1,1]

def bfs(w,h,i,j,arr,visited):
    queue=deque()
    queue.append((i,j))
    if arr[i][j]==0:
        return False
    if visited[i][j]==1:
        return False
    visited[i][j]=1
    while queue:
        x,y=queue.popleft()
        for k in range(8):
            nx=x+dx[k]
            ny=y+dy[k]
            if nx<0 or nx>h-1 or ny<0 or ny>w-1:
                continue
            if visited[nx][ny]==1:
                continue
            if visited[nx][ny]==0 and arr[nx][ny]==1:
                queue.append((nx,ny))
                visited[nx][ny]=1
    return True

result=[]
while True:
    w,h=map(int,input().split())
    count=0
    arr=[]
    if w==0 and h==0:
        break
    for i in range(h):
        tmp_list=list(map(int,input().split()))
        arr.append(tmp_list)
    visited=[[0 for i in range(w)]for j in range(h)]
    for i in range(h):
        for j in range(w):
            if bfs(w,h,i,j,arr,visited):
                count+=1

    result.append(count)

for i in result:
    print(i)