n= int(input()) # 출석번호 부른 횟수
a= input().split() # 무작위로 부른 번호
for i in range(n):
    a[i]=int(a[i])
d=[]
for i in range(23):
    d.append(0)    #[0,0,...0,0]처럼 0을 24번 차곡차곡 넣음
for i in range(n):
    d[a[i]-1]+=1     #a[i]번째 값을 인덱스로 사용. 예) a[i]번쨰 값이 3이면 3번에 카운트 1증가
for i in range(24):
    print(d[i], end=' ')

