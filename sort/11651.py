n=int(input())
points=[]
for i in range(n):
    point=list(map(int,input().split()))
    points.append(point)

points.sort(key=lambda x:(x[1],x[0]))

for i in points:
    print(str(i[0])+' '+str(i[1]))

# lambda 매개변수 : 표현식