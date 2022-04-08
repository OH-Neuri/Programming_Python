a, m ,d , n =map(int,input().split())
sum=a
for i in range(n-1):
    sum=(sum*m)+d
print(sum)