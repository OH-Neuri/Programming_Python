A= int(input())
B= int(input())
C= int(input())
N=A*B*C
list = [0 for j in range(10)]
for i in range(9):
    list[(N%10)]+=1
    N=int(N/10)
    if N==0:
        break
for i in range(10):
    print(list[i])

