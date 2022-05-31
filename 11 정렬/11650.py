import sys
input = sys.stdin.readline

n=int(input())
a=[]
for i in range(n):
    x, y = map(int, input().split())
    a.append([x, y])
a.sort(key= lambda x: (x[0],x[1]))
for i in range(n):
    print(a[i][0], a[i][1])

# sort(key= lambda x: (x[0],x[1]): 요소들 정렬, 0번째 인덱스 순으로 정렬 후 중복시 1번쨰 인덱스로 정렬