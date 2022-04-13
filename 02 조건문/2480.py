s = list(map(int, input().split()))

if len(set(s))==1 : print(max(s)*1000+10000)
elif len(set(s))==2 : print(sorted(s)[1]*100+1000)
else : print(max(s)*100)

*_,a,b,c=sorted(input());print(['1'+b,c][a<b<c]+'000'[a<c:])

a,b,c=sorted(map(int,input().split()))
print([c,b+10,b*10+100][[a,b,c].count(b)-1]*100)

a,b,c=sorted(map(int,input().split()));k=100;print([[k*10+b*k,c*k][a<b and b<c],k*k+a*k*10][a==c])

A,B,C=map(int,input().split())
print(10000+A*1000 if A==B and A==C else 1000+A*100 if A==B or A==C else 1000+C*100 if B==C else max(A,B,C)*100)