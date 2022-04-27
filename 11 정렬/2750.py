import sys
input= sys.stdin.readline

N= int(input())
list = []
for i in range(N):
    list.append(int(input()))
list.sort()
for i in list:
    print(i)
