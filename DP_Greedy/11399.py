n=int(input())
members=list(map(int,input().split()))
result=0
for i in range(1,n+1): # 1 2 3 3 4
    tmp=result+i # 1, 3
    result+=sum(sorted(members)[:i]) #1, 

print(result)