#큐는 선입 선출 !
from collections import deque

n=int(input())
queue=deque()

queue.appendleft(n)

for i in range(n-1,0,-1):
    queue.appendleft(i) #3,4

    for j in range(i): #0부터 3까지
        newCard= queue.pop() #4를 뽑는다
        queue.appendleft(newCard) # 4을 맨앞에 둔다

for i in queue:
    print(i,end=' ')
