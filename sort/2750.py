n= int(input())
numbers=[]
for i in range(n):
    num=int(input())
    numbers.append(num)

numbers=sorted(numbers)

for i in range(n):
    print(numbers[i])
