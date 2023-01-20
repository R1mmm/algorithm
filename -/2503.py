# 숫자 야구
# 하나가 동일한 수, 동일한 자리에 위치-> 스트라이크
# 다른 위치에 있으면 => 볼

from itertools import permutations

n=int(input())

num=list(permutations([1,2,3,4,5,6,7,8,9],3)) #모든 순열 (순서가 다르면 다른 배열로 취급)

for _ in range(n):
    test,s,b=map(int,input().split()) # 숫자, 스트라이크 수, 볼 수 [123,1,1]
    test=list(str(test)) #숫자를 리스트 형태로 변경 ['1','2','3']
    remove_cnt=0

    #test 숫자가 들어오면 num리스트를 돌면서 해당하지 않는 수들을 빼낸다.
    for i in range(len(num)):
        s_cnt=b_cnt=0
        # i는 현재 num리스트값의 길이에 따라 설정되어있기 때문에, 리스트에서 삭제되면 for 문을 도는 i의 값도 그만큼 마이너스 해줘야한다.
        i-=remove_cnt

        for j in range(3):
            test[j]=int(test[j]) #문자로 변경되었던 요소 하나하나를 다시 숫자로 변경
            if test[j] in num[i]: #test[j]= '1' 이 num[i]에 있다면
                if j==num[i].index(test[j]): # 그리고, 그 위치가 같다면
                    s_cnt+=1 #스트라이크 +1
                else:
                    b_cnt+=1 #num[i]에 있긴한데, 그 위치가 다르면, 볼 +1
        if s_cnt != s or b_cnt !=b:
            num.remove(num[i])
            remove_cnt+=1


print(len(num))



# 전체적인 구조
# 1. 1-9의 숫자들 중 3개를 뽑아 만들어지는 모든 순열을 num에 넣는다.
# 2. 민혁이가 말한 숫자(test)가 입력되면, num리스트를 순회하면서 비교한다.
# 3. 입력받은 숫자(test)를 리스트 형태로 바꾼다. 123 => [1,2,3]
# 4. num리스트의 모든 순열을 돌면서 입력된 숫자와 비교한다. => if test[j] in num[i]: 
# 5. 순열에 있는 값이 (1,2,3)이라면 비교되는 숫자(test,[1,2,3])와의 비교를 통해 s_cnt가 3이 된다.
# 6. 이렇게 되면 입력된 1스트라이크 1볼과 맞지 않는 숫자(s_cnt=3, b_cnt=0)가 나오므로 (1,2,3)은 후보에서 제외되고, num에서 remove된다
# 7. 현재 for문이 len(num)을 기준으로 돌고 있기 때문에, list에서 삭제된다면 remove_cnt를 통해 i 또한 변경해주어야한다.


