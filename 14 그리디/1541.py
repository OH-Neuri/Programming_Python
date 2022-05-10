import sys
input = sys.stdin.readline

num= input()
numAdd='0'
list1=0
list2=0
cnt=0
for i in range(len(num)):
    if num[i]!='-':
        if cnt==0:
            if num[i]=='+' and num[i]=='-':
                list1+=int(numAdd)
                numAdd='0'
            else:
                numAdd.add(num[i])
        if cnt==1:
            if num[i]=='+' and num[i]=='-':
                list2+=int(numAdd)
                numAdd='0'
            else:
                numAdd.add(num[i])
    else:
        cnt+=1
print(list1-list2)



