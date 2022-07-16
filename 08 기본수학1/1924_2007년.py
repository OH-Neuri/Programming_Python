day=0
month=[31,28,31,30,31,30,31,31,30,31,30,31]
week =["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())
#총 일수
for i in range(x-1):
    day+=month[i]
#요일(요일은 계속 이어지니까)
day=(day+y)%7
print(week[day])