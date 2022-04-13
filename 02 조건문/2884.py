h, m= map(int,input().split())
x= h*60+m-45
print(x//60%24, x%60)