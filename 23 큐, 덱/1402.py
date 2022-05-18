import sys
input = sys.stdin.readline


N = int(input())
stack=list(map(int,input().split()))
for i in range(N):
    print(stack.pop(), end=' ')
