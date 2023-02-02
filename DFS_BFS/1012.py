import sys
input=sys.stdin.readline
t=int(input())
sys.setrecursionlimit(10**6)
def dfs(x,y):
    global field
    global rows
    global cols
    if x<=-1 or y<=-1 or x>=rows or y>=cols:
        return False

    if field[x][y]==1:
        field[x][y]=0

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True

    return False


result=[]
for i in range(t):
    count=0
    rows,cols,k=map(int,input().split())
    field=[[0 for j in range(cols)] for i in range(rows)]
    for j in range(k):
        x,y=map(int,input().split())
        field[x][y]=1
    
    for n in range(rows):
        for m in range(cols):
            if dfs(n,m)==True:
                count+=1

    result.append(count)

    
for i in result:
    print(i)