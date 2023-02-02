n=int(input())
maps=[]
for i in range(n):
    tmp=map(int,input())
    maps.append(list(tmp))

result=[]
count=0

def dfs(x,y):
    global count
    if x<= -1 or x>=n or y<=-1 or y>=n:
        return False
    
    if maps[x][y]==1:
        count+=1
        maps[x][y]=0

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            result.append(count)
            count=0
           
print(len(result))
for i in sorted(result):
    print(i)
