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