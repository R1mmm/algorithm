t=int(input())
result=[]
for i in range(t):
    str_data=input()
    stack=[]
    tmp=0
    for j in str_data:
        if j=="(":
            stack.append("(")
        else:
            if(len(stack)==0): #empty를 활용해서 구현할 수 있을듯. 근데 귀차늠
                result.append("NO")
                tmp=1
                break
            else:
                stack.pop()
    if (tmp!=1):
        if (len(stack)>0):
            result.append("NO")
        else:
            result.append("YES")

for i in result:
    print(i)

# 스택에 ( 를 넣고
# )가 들어오면 스택에서 (를 없앤다
# 마지막에도 스택에 (가 남아잇거나, 스택에 (가 없는데 없애면 NO