import sys
input = sys.stdin.readline
from collections import Counter

N=int(input())
list=[]

for i in range(N):
    list.append(int(input()))

print(round(sum(list)/N))    #평균 구하는식

list.sort()
print(list[N//2]) #중앙값

cnt= Counter(list).most_common()
if len(cnt)>1 and  cnt[0][1]== cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(max(list)-min(list))
