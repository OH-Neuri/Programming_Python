

while True:
    try:
        print(input())
    except EOFError:
        break

'''
import sys
while True:
    try:
        print(sys.stdin.readline().rstrip())
    except EOFError:
        break
        
        sys.stdin.readline()이건 
input은 EOF를 받을 때 EOFError를 일으키지만 

sys.stdin.readline은 EOF를 받을 때 빈 문자열을 리턴합니다.

따라서 오류가 발생하지 않고 틀리게 됩니다.
'''