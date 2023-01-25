import sys
from collections import deque

count_1 = 0
count_2 = 0

arr=[0]
f=deque(arr)

def fibonacci(n):
    global count_2
    
    f.append(1)
    f.append(1)
    for i in range(3,n+1):
        count_2+=1
        f.append(f[i-1] + f[i-2])  # 코드2
    return f[n]


n=int(sys.stdin.readline())
count_1=fibonacci(n)
print(count_1,n-2)