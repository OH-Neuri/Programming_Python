import sys
input = sys.stdin.readline

x, y, X, Y = map(int,input().split())
if (X-x)>(Y-y):
    print(Y-y)
else:
    print(X-x)