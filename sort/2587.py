numbers=[]
for i in range(5):
    num=int(input())
    numbers.append(num)

print(int(sum(numbers)/5))
print((sorted(numbers))[2])
