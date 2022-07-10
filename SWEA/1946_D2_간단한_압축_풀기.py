T = int(input())

for i in range(1,T+1):
    N= int(input())
    text=''
    for n in range(N):
        a, b = input().split()
        text+=a*int(b)
    print('#%d' %(i))
    for j in range(1, len(text)+1, 10):
        print(text[j-1:j+9])