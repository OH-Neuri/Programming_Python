a, r, n=map(int, input().split())
sum=0
for i in range(n):
    sum=a*(r**i)
print(sum)