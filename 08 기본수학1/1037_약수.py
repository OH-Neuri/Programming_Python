N= int(input())
num=[x for x in map(int,input().split())]
num.sort()
print(num[0]*num[N-1])