n=int(input())
points=[]
for i in range(n):
    point=list(map(int,input().split()))
    points.append(point)

for i in sorted(points):
    print(str(i[0])+' '+str(i[1]))