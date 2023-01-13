# 스택은 후입선출!
# 가장 최근에 재민이가 쓴 수를 지우게 시킨다 -> stack에서 top에 있는 데이터를 뺀다

k=int(input())
stack=[]
for i in range(k):
    num=int(input())
    if (num==0):
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))