n= list(input())

num=[0] *10
for i in n :
    if int(i) == 9:
        num [6] +=1
    else:
        num[int(i)] +=1
if num[6] %2==0:
    num[6] = num[6]//2
else:
    num[6]%2!=0
    num[6] = (num[6]//2)+1
print(max(num))