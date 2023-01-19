n=int(input())
result=[]
for i in range (1,n+1):
    num=i
    n2=i #1 / 1
    n1=n #100 / 1 
    tmp_list=[n1] 
    while num>=0:
        tmp_list.append(num)
        num=n1-n2
        n1=n2
        n2=num
    
    if len(tmp_list)>len(result):
        result=tmp_list

s=' '.join([str(n) for n in result])
print(len(result))
print(s)
        