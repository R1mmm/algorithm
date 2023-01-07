import sys

n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))

#오름차순 정렬이기에 결국 이 리스트에서의 인덱스 값 = 압축 좌표값이 됨
tmp_list=sorted(list(set(nums)))

dic={tmp_list[i]: i for i in range(len(tmp_list))}
for i in nums:
    print(dic[i],end=' ')


# 시간초과 풀이
# 이건 왜 안 될까???len으로 접근해서 그런감
# for i in nums:
#     print(len(list(filter(lambda x : i>x, set(nums)))),end=" ")