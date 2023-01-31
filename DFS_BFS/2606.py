# BFS로 풀어보자!
from collections import deque

def bfs(arr,v,visited):
    visited[v]=True
    queue=deque([v])

    while queue:
        v=queue.popleft()
        for i in arr[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


n=int(input())
m=int(input())
arr=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,(input().split()))
    arr[a].append(b)
    arr[b].append(a)

visited=[False]*(n+1)
bfs(arr,1,visited)

print(visited.count(True)-1)