'''
x = int(input('첫 번째 숫자를 입력하시오:'))
y = int(input('두 번째 숫자를 입력하시오:'))

if x > 0 and y > 0:
    print("1")
if x < 0 and y > 0 :
    print("2")
if x > 0 and y < 0:
    print('3')
if x < 0 and y < 0:
    print('4')

n = int(input('숫자를 입력하시오'))
f = 0


for i in range(1,10):
    f += 1
    print(f'{n} * {f} = {n*f}' )
    '''


while True:
    print('정수 2개를 입력하시오')

    x = int(input('첫 번째 정수를 입력하시오: '))
    y = int(input('두 번째 정수를 입력하시오: '))

    factorial_x = 1
    factorial_y = 1

    for i in range(1, x + 1):
            factorial_x *= i
    for i in range(1, y + 1):
            factorial_y *= i

    if x == 0 or y == 0:
        print('프로그램을 종료합니다')
        break

    elif x > 0 and y > 0 :
            print(f' 첫 번째 수의 팩토리얼 값은 {factorial_x} 입니다.')
            print(f' 두 번쨰 수의 팩토리얼 값은 {factorial_y} 입니다.')
            
    print(f'두 팩토리얼 값의 차(절대값은)는 {abs(factorial_x - factorial_y)} 입니다.')          

           


