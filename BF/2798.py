n,m= map(int,input().split())
nlist= list(map(int,input().split()))
result=0
for i in range(len(nlist)-2):
    tmp_result=0
    for j in range(i+1,len(nlist)-1):
        for k in range(j+1,len(nlist)):
            tmp_result=nlist[i]+nlist[j]+nlist[k]
            if tmp_result<=m and tmp_result>result:
                result=tmp_result
print(result)