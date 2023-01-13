import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque(enumerate(map(int, sys.stdin.readline().split())))
result = []

while (len(queue)>0):
    index, nums = queue.popleft() # (0,3) (3,-3)
    result.append(index + 1) # 1 4

    if (nums > 0): # 3
        queue.rotate(-(nums - 1)) # (3,-3) , (4,-1) , (1,2) , (2,1)
    else:
        queue.rotate(-nums) # 중요한점은 양수일 때 시계방향으로 회전하므로, nums가 음수일땐 -를 곱하여 해결해주어야한다.

print(' '.join(map(str, result)))