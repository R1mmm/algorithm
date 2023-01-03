import sys

N = int(sys.stdin.readline())
num_list = [0] * 10001
#계수 정렬을 사용해보자
#인덱스값- 해당하는 숫자 / 인덱스에 들어간 값 - 숫자 카운트

for i in range(N):
    n = int(sys.stdin.readline())
    num_list[n]+=1

for i in range(10001):
    if(num_list[i] > 0):
        for j in range(num_list[i]):
            print(i)
