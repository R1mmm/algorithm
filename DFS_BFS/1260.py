from collections import deque

def dfs(graph, v, visited):
    print(v,end=" ")
    visited[v]=True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph, v, visited):
    queue=deque([v])
    visited[v]=True

    while queue:
        v=queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


n,m,start=map(int,input().split())
arr=[[] for _ in range(n+1)]
# print(arr)
for i in range(m):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1,n+1):
    arr[i].sort()
# print(arr)
arr2=arr[:]
visited = [False] * (n+1)
visited2 = visited[:]


dfs(arr,start,visited)
print()
bfs(arr2,start,visited2)
