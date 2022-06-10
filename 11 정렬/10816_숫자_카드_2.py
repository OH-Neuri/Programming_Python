import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))

hashmap = {} #카운트 수 담아 놓을 딕셔너리
for i in a: # 카운트 될 수
    if i in hashmap:  #카운트 수가 없다면 1, 있으면 +=1
        hashmap[i] += 1
    else:
        hashmap[i] = 1

for i in b: # 카운트 몇번 됐는지 확인
    if i in hashmap: # 카운트 되었으면 출력, 없으면 0 출력
        print(hashmap[i], end=" ")
    else:
        print(0, end=" ")
print()

'''
잘못되었다는 것은 아닌데 이 경우 M과 N의 값이 매우 크다는 것을 인식한다면
단순한 이분검색으로는 시간초과가 뜰 것이라는 것을 예상할 수 있습니다.
이분검색으로 될 수도 있겠지만 앞에 말한대로 M, N 의 값을 봤을 때 다른 방향을
생각하는 것이 맞다는 의미입니다.

이런 경우 이분검색보다는 hashmap 을 사용하는 것이 옳은 방향입니다.
처음 기존에 있던 값들을 count 하는데는 약간의 시간이 걸리지만 M 에 있는
값들을 찾는 것은 매우 빠르게 수행할 수 있으니까요.

파이썬에서 hashmap 은 아시다시피 dictionary 입니다.
'''