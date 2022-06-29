import sys
input = sys.stdin.readline

while True:
    num=list(map(int, input().split()))
    num.sort()
    if num[0]==num[1]==num[2]==0:
        break
    if num[0]**2+num[1]**2==num[2]**2:
        print("right")
    else:
        print("wrong")
