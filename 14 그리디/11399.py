import sys
input = sys.stdin.readline

N=int(input())
num=list(map(int,input().split()))
M =0
result=0

num.sort()
for i in range(len(num)):
    M+=num[i]
    result+=M
print(result)