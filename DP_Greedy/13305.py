# 현재 price를 저장해두고, distance를 계속 더해가다가 나보다 작은 프라이스가 나오면
# 축적된 distance*price를 하고, distance는 0으로 초기화, 현재 price는 나보다 작은 프라이스로 바꿔준다
city_num=int(input())
distance=list(map(int,input().split()))
price=list(map(int,input().split()))

result=0
current_price=price[0]
current_distance=distance[0]

for i in range(1,city_num-1):
    if current_price>=price[i]:
        result+=current_distance*current_price
        current_price=price[i]
        current_distance=0
        current_distance+=distance[i]
    else:
        current_distance+=distance[i] 
    
    if i==city_num-2:
        result+=current_distance*current_price
        
    
print(result)