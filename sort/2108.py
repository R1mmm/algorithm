from collections import Counter
import sys

n=int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range (n)]

numbers.sort()

print(round(sum(numbers)/n)) #산술평균
print(numbers[n//2]) #중앙값


# dic={}
# for i in range (n):
#     dic[numbers[i]]=0

# for i in numbers:
#     dic[i]+=1

# tmp = [k for k,v in dic.items() if max(dic.values()) == v]
tmp = Counter(numbers).most_common(2)
# print(tmp)
# print(len(tmp))
if(len(tmp)>1):
    if (tmp[0][1] == tmp[1][1]):
        print(tmp[1][0])
    else:
        print(tmp[0][0])
else:
    print(tmp[0][0])


#print(most_common_value.most_common()) #최빈값
print(max(numbers)-min(numbers)) #범위
