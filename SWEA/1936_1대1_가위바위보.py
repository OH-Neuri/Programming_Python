A, B= map(int,input().split())

if A>B:
    if A-B==1:
        print('A')
    else:
        print('B')
elif B-A==2:
    print('A')
else:
    print('B')