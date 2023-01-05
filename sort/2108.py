import sys

n=int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range (n)]

numbers.sort()

print(round(sum(numbers)/n)) #산술평균
print(numbers[n//2]) #중앙값

dic={}
for i in range (n):
    dic[numbers[i]]=0

for i in numbers:
    dic[i]+=1

tmp = [k for k,v in dic.items() if max(dic.values()) == v]

if(len(tmp)>1):
    print(sorted(tmp)[1]) #최빈값
else:
    print(sorted(tmp)[0]) #최빈값

print(max(numbers)-min(numbers)) #범위
