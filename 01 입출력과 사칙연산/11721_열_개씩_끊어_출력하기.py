from collections import deque

text=deque(input())
while len(text)>0:
    for i in range(10):
        print(text.popleft(),end='')
        if len(text)==0:
            break
    print()