def selfNum():
    numList = list(range(1,10001)) #1~10000 리스트 생성
    notSelfNumList =[] # 셀프넘버가 아닌 숫자를 담을 리스트 생성
    for i in numList:
        for k in str(i):  #숫자열을 문자열로 변환하고
            i += int(k)   #문자열들의 각 문자들을 i에 더해준다
        if i<=10000:  # 그 더한 값이 10000보다 작거나 같은 값에 속한다면, 생성자가 있는 숫자다.
            notSelfNumList.append(i)
    for y in set(notSelfNumList):
        numList.remove(y)
    for z in numList:
        print(z)
selfNum()