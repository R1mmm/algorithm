from collections import deque

n=int(input())
per1,per2=map(int,input().split())
m=int(input())
relation=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]


for i in range(m):
    x,y=map(int,input().split())
    relation[x].append(y)
    relation[y].append(x)


def bfs(x,y):
    q=deque()
    q.append((x,0))
    visited[x]=1

    while q:
        now,cnt=q.popleft()
        if now==y:
            return cnt
        visited[now]=1
        cnt+=1
        for i in relation[now]:
            if visited[i]==0:
                q.append((i,cnt))
    
    return -1

answer=bfs(per1,per2)
print(answer)

