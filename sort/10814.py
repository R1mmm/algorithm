import sys

n=int(sys.stdin.readline())
users=[]
for i in range (n):
    user=list(sys.stdin.readline().split())
    users.append(user)

for i in (sorted(users,key = lambda user: int(user[0]))):
    print(i[0],i[1])