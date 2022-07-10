'''
T=int(input())
for i in range(T):
    str=input()
    if str==str[::-1]:
        print("#%d 1" %(i+1))
    else:
        print("#%d 0" %(i+1))

'''

for i in range(6):
    for j in range(6):
        index=i+j
    print("index : %d i : %d j : %d" %(index, i ,j))

