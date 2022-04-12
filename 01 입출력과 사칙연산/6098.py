d=[list(map(int,input().split()))for _ in range(10)]
x=1
y=1

while 1:
    if x==9 and y==9: #가장 끝 만나면 탈출
       d[x][y]=9
       break

    if d[x][y]==0:  #자리에 9찍고 만약 2를 만나면 9찍고 탈출
        d[x][y]=9
    elif d[x][y+1]==2:
        d[x][y+1]=9
        break
    elif d[x+1][y]==2:
        d[x+1][y]=9
        break

    if d[x+1][y]==1 and d[x][y+1] ==1: # 아래, 오른쪽 1로 막혀있으면 탈출
        break

    if d[x][y+1]==0: # 오른쪽이 0이면 y 증가> 오른쪽 이동
        y+=1
    elif d[x+1][y]==0: # 아해가 0 이면 x 증가> 아래로이동
        x+=1

for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()

