import sys
n = int(sys.stdin.readline())
stack=[]
result=[]
for i in range (n):
    command=sys.stdin.readline().split()
    if (len(command)>1):
        stack.append(command[1])
    else:
        if(command[0]=="top"):
            if(len(stack)==0):
                result.append("-1")
            else:
                result.append(stack[-1])
        elif(command[0]=="size"):
            result.append(len(stack))
        elif(command[0]=="empty"):
            if(len(stack)==0):
                result.append("1")
            else:
                result.append("0")
        elif(command[0]=="pop"):
            if(len(stack)==0):
                result.append("-1")
            else:
                result.append(stack.pop())
        
for i in result:
    print(i)