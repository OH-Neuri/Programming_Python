N=input()
M=int(N)

Num=[0 for _ in range(10)]

for i in range(len(N)):
    Num[M%10]+=1;
    M=M//10

if Num[6]>=2:
    Num[6]= int(Num[6]/2)
if Num[9]>=2:
    Num[9] = int(Num[9]/2)

Num[6] = Num[6]+Num[9]
Num[9] = Num[6]

print(max(Num))
