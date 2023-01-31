# 점화식으로 나타내보자
# n=1 or n==2일때 dic[1] != dic[2]
# n=N일때 dic[n] != dic[n-1]
# 나머지는 dic[n+1]!=dic[n] and dic[n-1]!=dic[n]

# 엥 그냥 뭐가됐든 결국은 앞에 있는거랑 색 다르면 되는거 아닌가...

# -------------------------------(모르겠어서 결국 풀이 봄)

# 현재 더해지는 칸을 RGB, 012로 두고 그전에 계산된 값 중에서 나와 같지 않은 값 중 최소값을 더해주면 됨

n=int(input())
costs=[0]*n

for i in range(n):
    costs[i] = list(map(int,input().split()))

for i in range(1,n):
    costs[i][0] += min(costs[i-1][1],costs[i-1][2])
    costs[i][1] += min(costs[i-1][0],costs[i-1][2])
    costs[i][2] += min(costs[i-1][0],costs[i-1][1])


print(min(costs[n-1][0],costs[n-1][1],costs[n-1][2]))
