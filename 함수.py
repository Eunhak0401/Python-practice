if __name__ == '__main__':
#길이 함수
 '''
 def cm():
    print( num,'mm -->',num * 0.1 ,'cm')
def m():
    print( num,'mm -->',num * 0.001 ,'m')
def inch():
    print( num,'mm -->',num * 0.0393701 ,'inch')
def ft():
    print( num,'mm -->',num * 0.00328084 ,'ft')
def calculator():
    if (num > 0):
        cm(), m(), inch(), ft() 



num = int(input('숫자를 입력하시오:'))
calculator()

 #연산자 함수
def add():
    print('덧셈결과:', num1 + num2)
def sub():
    print('뺄셈결과:', num1 - num2)
def mul():
    print('곱셈결과:', num1 * num2)
def div():
    print('나눗셈결과:', num1 / num2)
def remain():
    print('나머지:', num1 % num2)
def calculator():
        if (Operator == 1):
                add()
        if (Operator == 2):
                sub()
        if (Operator == 3):
                mul()
        if (Operator == 4):
                div()
        if (Operator == 5):
                remain()

num1 = int(input("첫 번째 숫자를 입력하시오: "))
num2 = int(input("두 번째 숫자를 입력하시오: "))
Operator = int(input("연산자를 선택하세요: "))
calculator()

#팩토리얼 함수
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(10))
'''
#파보나치 함수
def Fibonacci(n):
    if n <= 0:
     return 0
    elif n == 1:
     return  1
    else:
     return Fibonacci(n - 1) + Fibonacci(n - 2)


print(Fibonacci(10))
