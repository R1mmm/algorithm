n=int(input())
valid=0
for i in range(1,n+1):
    each=0
    real_i=i
    while (i>0):
        each+=i%10
        i=i//10
    if (real_i+each==n):
        print(real_i)
        valid=1
        break

if (valid==0):
    print(0)