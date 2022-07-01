import sys
input = sys.stdin.readline

num=[x for x in map(int,input().split())]
num1=num.sort()
num2=num.sort(reverse=True)
if num==num1:
    print('ascending')
elif num==num2:
    print('descending')
else:
    print('mixed')
