import sys
input = sys.stdin.readline

k = int(input())
stack=[]
i=0
while i<k:
    i+=1
    n= int(input())
    stack.append(n)
    if n==0:
        stack.pop()
        stack.pop()
print(sum(stack))
