from itertools import combinations

len=[]
cnt=0
for i in range(9):
    len.append(int(input()))#[20, 7, 23, 19, 10, 15, 25, 8, 13]
c=list(combinations(len,7))

for i in c: # 조합으로 리트스에서 7개만 가져옴
    if sum(i)==100:
        d=list(i)
        d.sort()
        for j in d:
            print(j)
        break




