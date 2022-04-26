import sys
si = sys.stdin.readline
N = int(si().rstrip())

cnt = 0
for i in range(1, N+1):
    if i < 100:
        cnt+=1
    elif i<1000:
        if i//100+ i%10 ==((i-(i//100)*100)//10)*2:
            cnt+=1
    else:
        continue
print(cnt)