import sys
input = sys.stdin.readline

a,b = map(int,input().split())
n_heard = list()
n_hs = list()
for i in range(a+b):
    n_heard.append(input())
n_heard.sort()
i = 0
while i<a+b-1:
    if n_heard[i] == n_heard[i+1]:
        n_hs.append(n_heard[i])
        i+=2
    else:
        i+=1
print(len(n_hs))
for i in range(len(n_hs)):
    print(n_hs[i])