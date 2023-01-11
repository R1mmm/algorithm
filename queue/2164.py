from collections import deque
# 제일 위에 있는 카드를 바닥에 버림: popleft
# 제일 위에 잇는거 제일 밑으로: top 뽑아내고, 다시 어펜드
# 
n= int(input())
nlist= [i+1 for i in range(n)]
queue=deque(nlist)

while (len(queue)>1):
    queue.popleft()
    top=queue.popleft()
    queue.append(top)
    
print(queue[0])