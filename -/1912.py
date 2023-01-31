import sys
n=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))

max_num=numbers[0]
memoization=[numbers[0]]
for i in range(1,n):
    memoization.append(max(numbers[i],memoization[i-1]+numbers[i]))


    # memoization=list(map(lambda x : x+numbers[i], memoization))
    # memoization.append(numbers[i])
    # if max(memoization) > max_num:
    #     max_num=max(memoization)

print(max(memoization))