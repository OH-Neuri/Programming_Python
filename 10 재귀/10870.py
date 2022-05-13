import sys
input = sys.stdin.readline

n= int(input())
list= list(range(n+1))
list[0]=0
if n>=1:
    list[1]=1

for i in range(2, n+1):
    list[i]=list[i-1]+list[i-2]

print(list[n])