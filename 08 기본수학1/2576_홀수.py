
oddNum=[]
sum=0
for i in range(7):
    oddNum.append(int(input()))
for i in range(7):
    if oddNum[i]%2!=0:
        sum+=oddNum[i]
    else:
        oddNum[i] =99;

print(sum)
oddNum.sort()
print(oddNum[0])
