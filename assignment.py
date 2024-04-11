# 자동차 주행 속도를 숫자와 색상으로 표현
# 조건1. 현재속도 입력, 0이면 프로그램 종료
# 조건2. 속도를 숫자와 신호등으로 표시

import turtle 

speed = int(input('주행 속도를 입력하시오: (0입력시 종료)')) #주행속도 입력

t = turtle.Pen() 

while True:  #while문으로 종료 될 때까지 반복
    if speed == 0:
        turtle.done()
    break

if speed >= 40: #만약 주행속도가 40km/s이상이면 빨간색
    print('현재 주행속도는', speed ,'km/s입니다\n')
    print('속도를 줄이세요')
    t.fillcolor("red")
    
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.up()
    t.goto(0,-210)
    t.down()

    t.circle(100)

else:        #만약 주행속도가 40km/s이하이면 녹색
    print('현재 주행속도는', speed ,'km/s입니다\n')
    print('안전합니다')
    t.fillcolor("green")
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    
    t.up()
    t.goto(0, 210)
    t.down()

    t.circle(100)

turtle.done()