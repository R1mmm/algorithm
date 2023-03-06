# from collections import deque

s=input()
t=input()
result=0
# def bfs():
#     global result
#     q=deque()
#     q.append(s)

#     while q:
#         n_str=q.popleft()

#         if n_str==t:
#             result=1
#             return

#         if len(n_str)>len(t):
#             result=0
#             return
#         q.append(n_str+'A')
#         q.append("".join(reversed(n_str))+'B')
while t!=s:
    if t[-1]=='A':
        t=t[:-1]
    else:
        t=t[:-1]
        t="".join(reversed(t))
    if len(t)==len(s) and t!=s:
        break
    if t==s:
        result=1
        break

# bfs()
print(result)