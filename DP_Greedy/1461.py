book,max_book=map(int,input().split())
position=list(map(int,input().split()))

answer=0
real_position=sorted(position,reverse=True,key=lambda x:abs(x))
visited=[0 for _ in range(book)]
# print(real_position)
if book==1:
    print(1)
    exit(0)
while 0 in visited:
    # max_num=real_position[0]
    for i in range(len(real_position)):
        if visited[i]==0:
            max_num=real_position[i]
            visited[i]=1
            break
    # print(max_num)
    cnt=1
    i=0
    while cnt!=max_book and i<book:
        if real_position[i]*max_num>0 and visited[i]==0:#같은 부호라면
            visited[i]=1
            cnt+=1
        i+=1

    if answer==0:
        answer+=abs(max_num)
    else:
        answer+=(abs(max_num)*2)

print(answer)