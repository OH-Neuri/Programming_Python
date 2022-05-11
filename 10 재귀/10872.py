import sys
input = sys.stdin.readline
n= int(input())
def fn(n):
    if n<=1:
        return 1
    else:
        return n*fn(n-1)

print(fn(n))