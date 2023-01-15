n=int(input())
# 1부터 차례대로 push를 해주다가, top이 지금 수열에 해당하는 거면 pop해온다.
# 다음 num을 받았을때, 스택의 top 값이 num보다 크면 NO를 출력한다.
stack=[]
result=[]
numbers=[]

for i in range(n):
    num=int(input()) # 4 / 3
    numbers.append(num)
max_length=0
count=0
for i in numbers:
    if (len(stack)>0 and stack[-1]>i):
        print('NO')
        count=1
        break
    for j in range(max_length,i): 
        stack.append(j+1) 
        result.append('+')
        max_length=i
    if (len(stack)>0 and stack[-1]==i): 
            stack.pop()
            result.append('-')

if(count==0):   
    for i in result:
        print(i)
