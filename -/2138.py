from collections import deque

n=int(input())

current_state=input()
current_state=list(current_state)

wanted_state=input()
wanted_state=list(wanted_state)

memo=[]

step=0
result=0
q=deque()
q.append((current_state,step))
memo.append(current_state)


while q:
    current_arr,current_step=q.popleft()

    if current_arr==wanted_state:
        print(current_step)
        exit(0)

    for i in range(n):
        word=[]
        if i-1>=0:
            tmp_word= '1' if current_arr[i-1]=='0' else '0'
            word.append(tmp_word)
        tmp_word= '1' if current_arr[i]=='0' else '0'
        word.append(tmp_word)
        if i+1<n:
            tmp_word= '1' if current_arr[i+1]=='0' else '0'
            word.append(tmp_word)

        if i==0:
            word=word+current_arr[i+2:]
        elif i==n-1:
            word=current_arr[:-2]+word
        else:
            word=current_arr[:i-1]+word+current_arr[i+2:]
        
        if word not in memo:
            q.append((word,current_step+1))
            memo.append(word)


print(-1)