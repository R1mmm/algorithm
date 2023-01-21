# 정사각형이 될 수 있는 수는, n과 m 중에서 작은 수에 속한다
# for문으로 둘 중 작은 수 만큼 순회한다.
# 1x1 정사각형부터 min(n,m) x min(n,m) 까지 탐색한다.
# 만약 3,3 정사각형을 탐색하면, [0,0][0,2][2,0][2,2]를 탐색하고 같은지 확인한다

n,m=map(int,input().split())
num=[list(input()) for _ in range(n)]

# 1부터 n까지 늘려가면서 모든 배열을 순회하기 위해선 
# n,m 둘 중 작은거는 가장 위 for문에서 증가
# 큰거는 밑에서 1씩 증가
# 만약 2x2를 보려면 [0,0][0,1][1,0][1,1] / [0,1][0,2][1,1][1,2] 이렇게 순회해야함
# 만약 3x3를 보려면 [0,0][0,2][2,0][2,2] / [0,1][0,3][2,1][2,2] 이렇게 순회해야함

for i in range(min(n,m)):
    for j in range (n-i):
        for k in range (m-i):
            if num[j][k]==num[j][k+i]==num[j+i][k]==num[j+i][k+i]:
                result=(i+1)*(i+1)

print(result)
