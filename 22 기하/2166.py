import sys
input = sys.stdin.readline

N=int(input())
list=[]

for i in range(N):
    x, y =map(int,input().split())
    list.append([x, y])

list.sort(key=lambda x: x[0])
x1= list[N-1][0]-list[0][0]

list.sort(key=lambda x: x[1])
y1= list[N-1][1]-list[0][1]

print(f'{x1*y1:.1f}')
