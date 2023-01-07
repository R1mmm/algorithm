import sys

n=sys.stdin.readline()
# nList 얘를 set으로 안 하고 list로 하면,
# 뒤에 for 문 안에서 if x in nlist 이런식으로 확인할때,
# 리스트를 인덱스 0부터 n까지 일일이 검사를 해야해서 시간복잡도가 O(n),
# set에서 포함되어있는지 확인할때 시간복잡도는 O(1)
nList=set(sys.stdin.readline().split())
m=sys.stdin.readline()
mList=sys.stdin.readline().split()

print(' '.join(map(lambda x: '1' if x in nList else '0',mList)))