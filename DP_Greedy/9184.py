memoization={}
def w(a,b,c):
    # 셋중 하나라도 0보다 작아지면 return 값이 생긴다
    if a<=0 or b<=0 or c<=0:
        return 1

    if a>20 or b>20 or c>20:
        if (20,20,20) in memoization.keys():
            return memoization[(20,20,20)]
        else:
            memoization[(20,20,20)]= w(20,20,20)
            return memoization[(20,20,20)]
    

    if a<b and b<c:
        # for 문을 돌리면 if else문을 더 예브게 처리할 수 있을 거 같은데... 다음에 해볼게요
        if (a, b, c-1) in memoization.keys():
            A=memoization[(a, b, c-1)]
        else:
            A=w(a, b, c-1)
            memoization[(a, b, c-1)]=A
        
        if (a, b-1, c-1) in memoization.keys():
            B=memoization[(a, b-1, c-1)]
        else:
            B=w(a, b-1, c-1)
            memoization[(a, b-1, c-1)]=B

        if (a, b-1, c) in memoization.keys():
            C=memoization[(a, b-1, c)]
        else:
            C=w(a, b-1, c)
            memoization[(a, b-1, c)]=C

        return A+B-C
        
    else:
        if (a-1, b, c) in memoization.keys():
            A=memoization[(a-1, b, c)]
        else:
            A=w(a-1, b, c)
            memoization[(a-1, b, c)]=A

        if (a-1, b-1, c) in memoization.keys():
            B=memoization[(a-1, b-1, c)]
        else:
            B=w(a-1, b-1, c)
            memoization[(a-1, b-1, c)]=B

        if (a-1, b, c-1) in memoization.keys():
            C=memoization[(a-1, b, c-1)]
        else:
            C=w(a-1, b, c-1)
            memoization[(a-1, b, c-1)]=C

        if (a-1, b-1, c-1) in memoization.keys():
            D=memoization[(a-1, b-1, c-1)]
        else:
            D=w(a-1, b-1, c-1)
            memoization[(a-1, b-1, c-1)]=D

        return A+B+C-D
a=0
b=0
c=0
result=[]
while True:
    a,b,c=map(int,input().split())
    if a==-1 and b==-1  and c==-1 :
        break
    tmp=w(a,b,c)
    result.append("w(%i, %i, %i) = %i"%(a,b,c,tmp))

for i in result:
    print(i)