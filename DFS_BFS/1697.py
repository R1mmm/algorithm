from collections import deque
count=0
n,k=map(int,input().split())

def bfs(x):
    queue=deque()
    queue.append((x,0))
    visited=set()

    while queue:
        x,cnt=queue.popleft()
        if x-1==k or x+1==k or x*2==k:
            return cnt+1
        else:
            if x-1>=0 and x-1 not in visited:
                visited.add(x-1)
                queue.append((x-1,cnt+1))
            if x+1 < 100001 and x+1 not in visited:
                visited.add(x+1)
                queue.append((x+1,cnt+1))
            if x*2 < 100001 and x*2 not in visited:
                visited.add(x*2)
                queue.append((x*2,cnt+1))
           

if (n==k):
    print(0)
else:
    result=bfs(n)
    print(result)


# 확인 못했던 것들
# 1. 반례 처리 , n==k 인 경우
# 2. 중복된 숫자가 queue에 들어갈 경우 매우 비효율적이므로 visited를 통해 관리해줘야함
# 3. 점의 범위가 0<=n<=100,000이므로 범위를 조정해줘서 숫자를 넣어줘야함(범위를 벗어나는 숫자는 굳이 넣어줄 필요가 없으므로)