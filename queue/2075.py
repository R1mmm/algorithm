# 처음 값으로 힙을 구성한다.
# n번째 큰수 : 가장 큰 수 n개 중에 가장 작은 값
# 가장 큰 n개의 수로 힙을 유지하자
# 마지막엔 queue[0]하면됨
# 5 7 9 12 15
# 13 8 11 19 6

# 7 9 12 13 15
# 8 9 12 13 15
# 9 11 12 13 15
# 11 12 13 15 19


import heapq

n= int(input())
table=[]
for i in range(n):
    num_list = list(map(int, input().split()))
    if (len(table)==0): # 첫번째 입력
        for num in num_list:
            heapq.heappush(table, num) # 최소힙 구조
    else :
        for num in num_list: #num_list는 최소힙으로 구현돼있는 상태
            if(table[0]<num): 
                heapq.heappushpop(table,num) # num을 푸쉬하고, 가장 작은 값은 없애줌
            

    

print(table[0])