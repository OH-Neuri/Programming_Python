n = int(input())
a= input().split()
for i in range(n):          # a[0]~ a[n-1]
    a[i]= int(a[i])
for i in range (n-1,-1,-1): # a[n-1] ~a[0]
    print(a[i], end=' ')