#큐는 선입선출!
from collections import deque
import sys

queue = []

n=sys.stdin.readline()
for i in range(int(n)):
    command=sys.stdin.readline().split()
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if queue: print(queue.pop(0))
        else: print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(1-int(bool(queue)))
    elif command[0] == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif command[0] == 'back':
        if queue: print(queue[-1])
        else: print(-1)
    else:
        continue