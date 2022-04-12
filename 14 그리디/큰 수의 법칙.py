n, m, k = map(int, input().split())
d=list(map(int, input().split()))

sum=0
cnt=0
d.sort()
while True:     #.특정한 조건을 만족할때까지 반복
    for i in range(k): # 반복하다가 탈출 될 수 있으니까 반복문을 밖으로
        if m==0:       # 반복 하는 동안에 만약 m이 0이 된다면 탈출
            break
        sum+=d[n-1]    # sum에 최댓값 더하기
        m-=1           # 횟수 하나 빼기 (횟수를 무조건 반복문에 넣지 말것. 카운트로 써도됨)
    if m==0:           # 만약 0이 된다면 멈추기
        break
    sum+=d[n-2]        # 2번째 최댓값 더하기
    m-=1               # 카운트 줄이기

print(sum)