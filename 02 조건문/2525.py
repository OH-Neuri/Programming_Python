A, B = map(int,input().split())
C = int(input())
x= A*60+B+C
print(x//60%24, x%60)
