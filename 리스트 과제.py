studentNumber = [24001,24002]
studentName = ['박찬호', '손흥민']

print("[우리반 명부 관리]")

while True:
    print("[1]은 추가, [2]는 출력, [0]은 종료 ")
    num = int(input("선택:  "))

    if num == 0:
        print("종료합니다")
        break
    elif num == 1:
        num2 = int(input("학번:  "))
        num3 = str(input("이름:  "))
        studentNumber.append(num2)
        studentName.append(num3)
    elif num == 2:
        print('===============')
        print("학번 ㅣ 이름")
        print('----------------')
        for i in range(len(studentNumber)):
            print(studentNumber[i] | studentName[i])
            

