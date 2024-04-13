import turtle

while True:
    speed = int(input('속도를 입력하세요 (0을 입력하면 종료): '))
    t = turtle.Pen()
    t.circle(100)
    t.up()
    t.goto(250,0)
    t.down()
    t.circle(100)
    if speed == 0:
        turtle.done()
        break

    elif speed >= 40:
        print('현재 속도는', speed, 'km/s 입니다.')
        print('속도를 줄이세요')
        t = turtle.Pen()
        t.fillcolor("red")
        t.begin_fill()
        t.circle(100)
        t.end_fill()
    elif speed <=40:
        print('현재 속도는', speed, 'km/s 입니다.')
        print('안전합니다')
        t.up()
        t.goto(500, 0)
        t.down()
        t = turtle.Pen()
        t.fillcolor("green")
        t.begin_fill()
        t.circle(100)
        t.end_fill()

