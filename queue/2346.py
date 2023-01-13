import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque(enumerate(map(int, sys.stdin.readline().split())))
result = []

while (len(queue)>0):
    index, nums = queue.popleft()
    result.append(index + 1)

    if (nums > 0):
        queue.rotate(-(nums - 1))
    else:
        queue.rotate(-nums)

print(' '.join(map(str, result)))