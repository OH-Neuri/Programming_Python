import sys
input = sys.stdin.readline

N=int(input())
A = [ int(x) for x in input().split() ]
B=list(map(int,input().split()))
sum=0
A.sort()
B.sort(reverse=True)
for i in range(N):
    sum+=A[i]*B[i]
print(sum)