import sys
input = sys.stdin.readline

M, N= map(int,input().split())

for i in range(M,N):
    for j in range(2,N):
        if i%j==0:
            if i==j:
                print(i)
            break
