C= int(input())
for i in range(C):
    L= list(map(int, input().split()))
    avg = sum(L[1:])/L[0]
    cnt=0
    for k in L[1:]:
        if k > avg:
            cnt+=1
    res=cnt/L[0]*100
    print("{:.3f}%".format(res))