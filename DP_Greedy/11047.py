n,k=map(int,input().split())
kind=[]
result=0
for i in range(n):
    coin=int(input())
    kind.append(coin)

for i in (sorted(kind,reverse=True)):
    if i>k:
        continue
    else:
        result+=k//i
        k=k%i

print(result)