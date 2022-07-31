N=int(input())
num=[]
for i in range(N):
    num.append(int(input()))

if(sum(num)<= (N/2)-(0.5)):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")