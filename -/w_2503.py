from itertools import permutations

num_list=list(permutations([1,2,3,4,5,6,7,8,9],3))

n=int(input())

for _ in range(n):
    test,s,b= map(int,input().split())
    test=list(str(test))
    remove_cnt=0

    for i in range (len(num_list)):
        s_cnt=0
        b_cnt=0
        i-=remove_cnt
        for i in range (3):
            if int(test[i]) in num_list[i]:
                if i==num_list.index(int(test[i])):
                    s_cnt+=1
                else:
                    b_cnt+=1

        if s_cnt != s or b_cnt != b:
            num_list.remove(num_list[i])
            remove_cnt=1

print(len(num_list))