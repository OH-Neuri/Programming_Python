import sys
input = sys.stdin.readline

N= int(input())
case =[0] * 10001
for i in range(N):
    case[int(input())]+=1     #배열 인덱스에 입력값을 받고 그게 몇번 나왔는지 카운트
                              # 7을 입력 받으면 case[7]에 +1 카운트

for i in range(len(case)):
    if case[i]!=0:
        cnt=case[i]           #case[7]=3 일경우, cnt에 3 저장 후, 7을 3번 반복
        for j in range(cnt):
            print(i)
