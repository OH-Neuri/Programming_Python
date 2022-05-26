N = int(input())
result=[]
#단어 길이 정렬
for i in range(N):
    result.append(input())

result= list(set(result)) #set을 이용해 리스트의 중복요소 제거
result.sort() # 리스트 요소 알파벳 순서로 정렬
result.sort(key=len) # 리스트 요소를 길이 순으로 정렬

for i in result:
    print(i)

# 1181: 단어 정렬
# set: 리스트 요소 중복 제거 가능
# sort(key=len): 길이 순으로 정렬 가능