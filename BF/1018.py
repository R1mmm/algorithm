N,M=map(int,input().split())
table=[]

for i in range (N):
    row=input()
    table.append(list(row))

min_num=float("inf")

# 8x8의 형태로 잘라내서 검사한다
for i in range(N-7):
    for j in range (M-7):
        # table에서 row를 슬라이싱한 후, 슬라이싱된 row를 다시 col기준으로 슬라이싱하여 2차원배열을 만들어준다.
        split_table=[row[j:j+8] for row in table[i:i+8]]
        count_W=0 #W로 시작한다고 가정하는 경우
        count_B=0 #B로 시작한다고 가정하는 경우
        for k in range(8):
            for m in range (8):
                if ((k+1)%2==0 and (m+1)%2==0) or ((k+1)%2!=0 and (m+1)%2!=0): #row(k)+1와 col(m)+1이 홀짝이 같을때
                    if split_table[k][m] != "W":
                        count_W+=1
                    if split_table[k][m] != "B":
                        count_B+=1
                else:
                    if split_table[k][m] != "B":
                        count_W+=1
                    if split_table[k][m] != "W":
                        count_B+=1
        
        if min(count_B,count_W)<min_num:
            min_num=min(count_B,count_W)

print(min_num)

                    