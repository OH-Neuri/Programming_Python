N=int(input())
num=[x for x in map(int,input().split()) ]
num.sort()
print(num[int((N-1)/2)])