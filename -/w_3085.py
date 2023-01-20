
# 개인적인 생각은 answer가 n이 되면 반복문을 멈추고 빠져나와도 좋을듯 하다!

n=int(input())
candies=[list(input()) for _ in range(n)]
answer=1


def check(arr):
    answer=0

    # 행 체크
    for i in range(n):
        cnt=1
        for j in range (1,n):
            if arr[i][j-1] == arr[i][j]:
                cnt+=1
            else:
                cnt=1
            if cnt>answer:
                answer=cnt

    # 열체크
        cnt=1
        for j in range (1,n):
            if arr[j-1][i] == arr[j][i]:
                cnt+=1
            else:
                cnt=1
            if cnt>answer:
                answer=cnt

    return answer


for i in range(n):
    for j in range(n):
        # 오른쪽이랑 바꿔서 체크
        if j+1<n and candies[i][j] != candies[i][j+1] : # 오른쪽에 있는거랑 다르다면 바꾼다
            candies[i][j], candies[i][j+1] = candies[i][j+1],candies[i][j]
            
            temp=check(candies)

            if temp>answer:
                answer=temp
            
            candies[i][j], candies[i][j+1] = candies[i][j+1],candies[i][j]

        # 밑에랑 바꿔서 체크
        if i+1<n and candies[i][j] != candies[i+1][j] : # 밑에 있는거랑 다르다면 바꾼다
            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
            
            temp=check(candies)

            if temp>answer:
                answer=temp

            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]



print(answer)
            
    