import sys
input = sys.stdin.readline

N, M = map(int,input().split())
result=0
for i in range(N):
    num=list(map(int,input().split()))
    numMin=min(num)
    result=max(result,numMin)

print(result)