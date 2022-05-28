import sys
input = sys.stdin.readline

N=int(input()) #테스트 케이스
num = map(int,input().split())
cnt=0
for i in num:# 입력받은 수
    for j in range(2, i+1): # 1은 어차피 다 약수로 가지고 있으니 자기 자신까지 나눈 나머지를 검사
        if i % j ==0: # i=6, range(2,7) (2~6)
            if j ==i:
                cnt+=1
            break #나머지가 0일경우 다음 반복문으로 넘어가는데 이때 나눈 값이 자기 자신이면 cnt+=1
print(cnt)


