N=int(input())
A=N
cnt=0
while True:
    N= int(((N%10)*10)+(((N/10)+(N%10))%10))
    cnt+=1
    if N==A:
        break
print(cnt)

