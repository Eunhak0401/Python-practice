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
'''
n = int(input('숫자를 입력하시오'))
f = 0


for i in range(1,10):
    f += 1
    print(f'{n} * {f} = {n*f}' )