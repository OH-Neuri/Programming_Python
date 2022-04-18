N, X = map(int,input().split())
list =list(map(int, input().split()))
for i in range(N):
    if(list[i]<X):
        print(list[i], end=' ')
