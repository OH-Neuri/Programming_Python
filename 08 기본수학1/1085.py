import sys
input = sys.stdin.readline

x, y, X, Y = map(int,input().split())

print(min(x, y, (X-x), (Y-y)))
# print( min(x, y, (X-x), (Y-y))
# min, max 는 () 안에 있는 값들중 계산