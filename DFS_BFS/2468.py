from collections import deque
n=int(input())
area=[]
min_num=101
max_num=0
for i in range(n):
    tmp_arr=list(map(int,input().split()))
    area.append(tmp_arr)
    min_num=min(min_num,min(tmp_arr))
    max_num=max(max_num,max(tmp_arr))


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,num,visited):
    visited[x][y]=1
    q=deque()
    q.append((x,y))

    while q:
        nx,ny=q.popleft()

        for i in range(4):
            now_x=nx+dx[i]
            now_y=ny+dy[i]

            if now_x<0 or now_y<0 or now_x>n-1 or now_y>n-1:
                continue
            if visited[now_x][now_y]==0 and area[now_x][now_y]>num:
                q.append((now_x,now_y))
            visited[now_x][now_y]=1

    return visited

tmp_ans=0
answer=-1
for i in range(min_num-1,max_num+1):
    visited=[[0 for _ in range(n)] for _ in range(n)]
    tmp_ans=0
    for j in range(n):
        for k in range(n):
            if area[j][k]>i and visited[j][k]==0:
                visited=bfs(j,k,i,visited)
                tmp_ans+=1
    answer=max(answer,tmp_ans)

print(answer)