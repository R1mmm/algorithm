str=input()
numbers=[]
symbols=[0]
# 마이너스 뒤에 있는 + 기호 아이들을 한꺼번에 묶어주면 된다
tmp=''
for i in range (len(str)):
    if (i==len(str)-1):
        tmp+=str[i]
        numbers.append(int(tmp))
        break
    if str[i].isdigit():
        tmp+=str[i]
    else:
        symbols.append(str[i])
        numbers.append(int(tmp))
        tmp=''

tmp_sum=0
tmp_symbol="+"
result=0

# 55-50+40+30-20+30 
# symbols=[0,"-","+","+","-","+"]
# numbers=[55,50, 40, 30, 20, 30]
# -가 나올때까지 tmp_sum+=numbers[i]
for i in range(len(numbers)): #0,1,2,3,4
    if symbols[i]=="-":
        tmp_symbol="-"
        result-=tmp_sum
        tmp_sum=0
        tmp_sum+=numbers[i]
    else:
        if tmp_symbol=="-":
            tmp_sum+=numbers[i]
        else:
            result+=numbers[i] #55

    if i==len(numbers)-1:
        if tmp_symbol=="-":
            result-=tmp_sum

print(result)