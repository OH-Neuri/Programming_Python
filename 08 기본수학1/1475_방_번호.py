N=input()
M=int(N)
Num=[0 for _ in range(10)]

for i in range(len(N)):
    if M%10==9:
        Num[6]+=1;
    else:
        Num[M%10]+=1;
    M=M//10
if (Num[6]/2)%2==0:
    Num[6] = Num[6]/2
else:
    Num[6] = (Num[6] / 2)+1

print(int(max(Num)))
