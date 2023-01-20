# 사탕 게임
# 인접한 색이 다르면, 서로 바꿀 수 있다
# 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분을 먹는다
# 상근이가 먹을 수 있는 사탕의 최대 개수를 출력해보자

import sys
input=sys.stdin.readline

def check(arr): # 사탕의 위치를 바꾼 배열을 받는다
    n=len(arr)
    answer=1

    for i in range(n): # 처음 값부터 배열을 하나하나 순회한다.
        cnt=1
        for j in range(1,n): # 우측으로 비교 
            if arr[i][j] == arr[i][j-1]: #arr[0][1], arr[0][0] 비교, 
                cnt+=1
            else:
                cnt=1

            if cnt>answer:
                answer = cnt

        cnt=1
        for j in range(1,n): # 밑과 비교(열 기준으로 비교)
            if arr[j][i] == arr[j-1][i]: #arr[1][0], arr[0][0] 비교, arr[2][0], arr[1][0] 비교
                cnt+=1

            else:
                cnt=1

            if cnt>answer:
                answer=cnt
    return answer


n=int(input())
arr=[list(input()) for _ in range(n)]
answer=0

for i in range(n):
    for j in range(n):
        # arr[0][0] 부터 확인한다.
        # 앞에 있던 애들(상, 좌)는 이미 확인이 된 아이들이기 때문에 신경쓰지 않는다.
        # 즉 우리는 상,좌만 살필 것이므로 j+1, i+1이 n이 넘지 않게만 신경쓰면 된다
        # 오른쪽 사탕, 밑에있는 사탕을 바꾼 배열을 만든후, check에 넘겨서 하나하나 행과 열을 확인하여 연속된 사탕이 몇개 있는지찾아낸다.
        if j+1 <n: # 오른쪽 사탕과 바꾸기
            arr[i][j], arr[i][j+1] = arr[i][j+1],arr[i][j]

            temp=check(arr) # 우측 사탕과 바꾼 배열을 check에 보낸다

            if temp>answer:
                answer=temp

            arr[i][j], arr[i][j+1] = arr[i][j+1],arr[i][j]

        if i+1 <n:# 밑에 있는 사탕과 바꾸기
            arr[i][j], arr[i+1][j] = arr[i+1][j],arr[i][j]

            temp=check(arr)

            if temp>answer:
                answer=temp

            arr[i][j], arr[i+1][j] = arr[i+1][j],arr[i][j]

print(answer)



# 전체적인 아이디어
# 0,0 부터 n,n까지 테이블을 돌면서, 각각 오른쪽, 밑쪽이랑 바꾼다.
# 바꾼 배열을 check에 넣어서
# 모든열, 모든행을 다 확인해서 같은게 가장 많이 카운트 된숫자 (cnt)를 check의 answer에 넣는다. 그리고 answer을 리턴해줌
# 그걸 받아서, 메인의 answer와 비교하고 기존 answer보다 높으면 main의 answer에 넣어줌
# 바꿨던 배열은 다시 원래대로 바꿔준다