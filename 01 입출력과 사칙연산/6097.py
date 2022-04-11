h, w = map(int, input().split())

k= []
for i in range(h):
    k.append([])
    for _ in range(w):
        k[i].append(0)

n= int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    if d==0:
        for j in range(l):
            k[x-1][y+j-1]=1
    else:
        for j in range(l):
            k[x+j-1][y-1]=1

for i in range(h):
    for j in range(w):
        print(k[i][j], end=' ')
    print()

