from itertools import combinations

members=[]
for i in range(9):
    height=int(input())
    members.append(height)

seven=list(combinations(members, 7))

for i in seven:
    if sum(i)==100:
        result=i
        break

for i in sorted(result):
    print(i)