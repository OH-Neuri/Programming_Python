list =[0 for _ in range(10)]
for i in range(10):
    list[i]=int(input())%42
print(len(set(list)))

