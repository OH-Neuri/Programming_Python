N, K = map(int,input().split())
mon=[]
cnt=0
for i in range (N):
    mon.append(int(input()))
for i in mon[N::-1]:
    if i>K:
        continue
    if K>0:
        cnt+=K//i
        K%=i

print(cnt)

