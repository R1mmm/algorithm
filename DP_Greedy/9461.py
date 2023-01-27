# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
# 규칙
# n=1,2,3 일때 return 1
# n>3일때 n= n-2 + n-3

memoization={}
def p(n):
    if n==1 or n==2 or n==3:
        return 1
    if n in memoization.keys():
        return memoization[n]
    else:
        memoization[n]= p(n-3) + p(n-2)
        return memoization[n]

result=[]
t=int(input())
for i in range (t):
    n=int(input())
    result.append(p(n))

for i in result:
    print(i)

    