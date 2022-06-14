import sys
input = sys.stdin.readline


N=(input())
sum=0
if N.find('0')!=-1:
    for i in range(len(N)):
        sum+=int(N[i])
    if sum%3==0:
        N.sort(reverse=True)
    print(N)
else:
    print('-1')

    ## 아직 덜했음 ## 아직 덜했음 ## 아직 덜했음