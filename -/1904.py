from itertools import permutations
import math
n=int(input())

result=0
for i in range(int(n/2)+1): #0,1
    zero = i #1개
    one = n-(zero*2) #2개
    num = math.factorial(n)/math.factorial(n-zero+one)
    print(int(num))
    result+=num
    # tmp_list=['00']*i
    # tmp_list[len(tmp_list):len(tmp_list)] =['1']*(n-(len(tmp_list)*2))
    # num=set(list(permutations(tmp_list,len(tmp_list))))
    # result+=len(num)

print(int(result%15746))

#1,2,3,5,8,13 ㅇㄴ 걍 피보나치 수열이었어