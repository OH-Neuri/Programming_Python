score=[]
for i in range(5):
    num=int(input())
    if num>40:
        score.append(num)
    else:
        score.append(40)
print(int(sum(score)/5))