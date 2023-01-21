# n=int(input())
# tmp_num=-1 #몇번째 감소하는 수인지 체크
# result_num=-1 #감소하는 수인지 확인할 대상인 수
# valid=0
# while (tmp_num!=n):
#     result_num+=1
#     result_num_list=list(str(result_num))
#     if tmp_num==1023:
#         valid=1
#     # 감소하는 수가 아니라면
#     if ((sorted(result_num_list,reverse=True)) != result_num_list) or (len(set(result_num_list)) != len(result_num_list)):
#         continue
#     # 감소하는 수가 맞다면
#     else:
#         tmp_num+=1

# if valid==1:
#     print(-1)
# else:
#     print(result_num)



from itertools import combinations
# 시간 초과와 비효율적인 풀이인 첫번째 풀이를..고치기 위한 두번째 풀이
# 조합을 사용하여 0,1,2,3,4,5,6,7,8,9 를 사용한 모든 감소하는 수를 구해 배열을 만든다

n=int(input())
answer=[]

# 반복문을 통해 감소하는 수를 조합
# 최대 감소하는 수는 9876543210
for i in range(1,11):
    for j in combinations(range(10),i):
        print(j)
        num=sorted(list(j),reverse=True)
        answer.append(int("".join(map(str,num))))

answer.sort()
print(answer[n] if len(answer)>n else -1)