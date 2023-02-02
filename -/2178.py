# DFS를 사용해보자!
# 상하좌우로 이동할 수 있다.
# 우리가 체크해야하는건... 인접한 노드 중에 방문이 안 돼있고, 그 값이 1인 노드를 찾는것이다

from collections import deque

n,m=map(int,input().split())
arr=[]
for i in range(n):
    tmp=map(int,input())
    arr.append(list(tmp))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(nx,ny):
    queue=deque()
    queue.append((nx,ny))

    while queue:
        x,y=queue.popleft()

        if x==n-1 and y==m-1:
            return arr[x][y]

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx==-1 or ny==-1 or nx==n or ny==m:
                continue
            if arr[nx][ny]==0:
                continue
            if arr[nx][ny]==1:
                arr[nx][ny]=arr[x][y]+1
                queue.append((nx,ny))
        
        

result=bfs(0,0)
print(result)
