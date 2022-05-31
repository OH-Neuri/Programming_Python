import sys
input = sys.stdin.readline

n= int(input())
count=0
cnt=0
kg= [5, 3]

for x in kg:
    count+=n//x
    n%=x

print(count)