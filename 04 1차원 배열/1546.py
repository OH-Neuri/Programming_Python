N= int(input())
list = list(map(int,input().split()))
list1 = [i/max(list)*100 for i in list]
print(sum(list1)/N)