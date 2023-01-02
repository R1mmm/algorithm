
# 1) 삽입정렬
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입하는 정렬
# 자신을 기준으로 왼쪽에 있는 데이터들을 돌면서, 탐색한 데이터가 자기보다 크면, 자신과 그 데이터의 위치를 바꾼다.
# j-1이 자신(j)보다 작거나 같으면 이제 그만!

numbers=[5,7,9,0,3,1,6,2,4,8]

for i in range(1,len(numbers)):
    for j in range(i,0,-1):
        if (numbers[j] < numbers[j-1]):
            numbers[j] , numbers[j-1] = numbers[j-1] , numbers[j]
        else:
            break

print(numbers)


# ---------------------------------------
# 2) 선택정렬
# 처리되지 않은 데이터 중 가장 작은 데이터를 선택해서 맨 앞에 있는 애랑 바꾸기

numbers_2=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(numbers_2)):
    min_index=i
    for j in range(i+1,len(numbers_2)):
        if (numbers_2[j]<numbers_2[min_index]):
            min_index=j
        numbers_2[i],numbers_2[min_index] =numbers_2[min_index] ,numbers_2[i]

print(numbers_2)


# ---------------------------------------
# 3) 퀵정렬
# 기준데이터 피벗을 설정하고, 기준보다 큰 데이터(왼쪽에서부터), 작은데이터(오른쪽에서부터)의 위치를 바꾼다.

numbers_3=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start,end):
    if(start >= end): #원소가 1개면 종룔
        return
    pivot= start #피벗을 첫번째 원소로 설정
    left=start+1
    right=end
    while(left <= right):
        #왼쪽에서부터 피벗보다 큰 데이터를 찾기
        #큰 데이터를 찾으면 left에 큰 데이터의 인덱스가 저장됨
        while(left <=end and array[left] <= array[pivot]):
            left+=1
        #오른쪽에서부터 피벗보다 작은 데이터를 찾기
        #작은 데이터를 찾으면 right에 작은 데이터의 인덱스가 저장됨
        while(right >start and array[right] >= array[pivot]):
            right-=1

        #만약 둘이 엇갈렸다면, 작은 데이터와 피벗의 위치를 변경하고 재귀함수 실행하러 감
        if(left>right):
            array[right], array[pivot] = array[pivot], array[right]
        #안 엇갈렸다면, 가장 큰 데이터,가장 작은 데이터의 위치 변경
        else:
            array[right], array[left] = array[left], array[right]

    #right는 현재 피벗값의 위치
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)


quick_sort(numbers_3,0,len(numbers_3)-1)
print(numbers_3)