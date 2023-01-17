n=int(input())
members=[]
for i in range (n):
    member=list(map(int,input().split()))
    members.append(member)
ranks=[]
for i in range (n):
    rank=0 #처음엔 꼴찌로 시작해서
    for j in range(n):
        if (i==j):
            continue
        if (members[i][0]<members[j][0] and members[i][1]<members[j][1]):
            rank+=1

    ranks.append(rank+1)

for i in ranks:
    print(i,end=" ")