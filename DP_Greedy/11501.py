import sys
input=sys.stdin.readline

t=int(input())
result=[]

for i in range(t):
    n=int(input())
    prices=list(map(int,input().split()))
    gain=0
    
    if sorted(prices,reverse=True) == prices:
        result.append(0)
        continue
    
    while len(prices)>1:
        max_idx=prices.index(max(prices))
        if max_idx==0:
            prices=prices[1:]
            continue
        invest=sum(prices[:max_idx]) #가장 큰 숫자의 인덱스 전까지 합
        gain+=max(prices)*(max_idx)-invest
        prices=prices[max_idx+1:]

    result.append(gain)

for i in result:
    print(i)