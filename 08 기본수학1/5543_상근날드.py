hamPrice = []
coPrice = []
for i in range(3):
    hamPrice.append(int(input()))
for i in range(2):
    coPrice.append(int(input()))
hamPrice.sort()
coPrice.sort()
print((hamPrice[0]+coPrice[0])-50)