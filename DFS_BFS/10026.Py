import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
area=[]
area2=[]

for i in range(n):
    tmp=input()
    tmp_2=tmp.replace("R","G")
    area.append(list(tmp))
    area2.append(list(tmp_2))
visited_1=[[0 for i in range(n)]for j in range(n)]
visited_2=[[0 for i in range(n)]for j in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs_1(i,j):
    queue=deque()
    queue.append((i,j))

    if visited_1[i][j]==1:
        return False
    visited_1[i][j]=1
    color=area[i][j]

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or nx>n-1 or ny<0 or ny>n-1:
                continue
            if visited_1[nx][ny]==1:
                continue
            if area[nx][ny]==color:
                visited_1[nx][ny]=1
                queue.append((nx,ny))

    return True

def bfs_2(i,j):
    queue=deque()
    queue.append((i,j))

    if visited_2[i][j]==1:
        return False
    visited_2[i][j]=1
    color=area2[i][j]

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or nx>n-1 or ny<0 or ny>n-1:
                continue
            if visited_2[nx][ny]==1:
                continue
            if area2[nx][ny]==color:
                visited_2[nx][ny]=1
                queue.append((nx,ny))

    return True

count_1=0
count_2=0

for i in range(n):
    for j in range(n):
        if bfs_1(i,j):
            count_1+=1
        if bfs_2(i,j):
            count_2+=1


print(count_1,count_2)

