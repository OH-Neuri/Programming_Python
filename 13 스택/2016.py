from collections import deque
k= int(input())
n= int(input())
que=deque()
for i in range(k):
    que.append(n[i])
    n=n%(10*(k-i))
print(543//100)
'''
i =0
while k>0:
    print(que.pop(), end='')
    i+=1
    k-=1
    if i==3:
        print(',', end='')
        i=0
        k-=1
'''