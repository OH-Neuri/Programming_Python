N= int(input())
for i in range(N):
    list=input()
    cnt=0
    sum=0
    for j in range(len(list)):
        if list[j]=='O':
            cnt+=1
        if list[j]=='X':
            cnt=0
        sum+=cnt
    print(sum)


