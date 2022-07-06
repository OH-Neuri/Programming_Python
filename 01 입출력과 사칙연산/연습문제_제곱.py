'''
a=int(input())
b=0
while b<a:
    print(a)
    b+=1
'''

'''
a = int(input())
for i in range(a):
    print((i+1), (i+1)**2)
'''
'''
number = 358

rem = rev = 0
while number >= 1:
    rem = number % 10
    rev = rev * 10 + rem
    number = number // 10

print(rev)
'''

def triple(x):
    print(x*3)
print(triple(2))