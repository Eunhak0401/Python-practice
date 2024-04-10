#sep ''사이에 넣기
""" 
print('p', 'y', 't', 'h', 'o', 'n', sep='')
print('python', 'google', sep='@')

#end 한줄에 표기

print('welcome to', end=' ')
print('IT Nesws', end=' ')
print('Web Site', end=' ')

# file 외부 파일에 실행

import sys
print('Learn Python', file=sys.stdout)
print()

#format (d : 3,s : 'python' ,t : 3.14454545)
print('%s %s' % ('one','two'))    # format은 {} 사이에 넣기 앞에 .필수
print('{} {}' .format('one', 'two'))
print('{1} {0}' .format('하나', '둘'))

# %s
print('%10s' % ('nice'))
print('{:>10}' .format('nice'))
print('{:>30}' .format('nice'))     #{:>10}은 칸 벌리기 

print('%-10s' % ('nice'))
print('{:10}' .format('nice'))


print('{:^>10}' .format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))       #.을 5s앞에 붙이면 5글자만 나옴
print('%5s' % ('pythonstudy'))
print('{:10.10}' .format('pythonstudy'))

# %d
print('%d %d' % (1, 2))
print('{} {}' .format(1,2))

print('%4d' % (42))
print('{:4d}' .format(42))


# %f
print('%1.8f' % (3.13131313131313131313))
print('{:f}' .format(3.131313131313))

print('%06.1f' % (3.132424242424242))
print('%06.2f' % (3.131313131313131))

# 3가지 Format Practices

x = 50
y = 100
text = 308276567
n = 'Lee'

# 출력1
ex1 = 'n = %s, s = %s, sum=%d' % (n, text, (x + y))
print(ex1)

# 출력2
ex2 = 'n = {n}, s = {s}, sum={sum}' .format(n=n, s=text, sum=x+y)
print(ex2)

#출력3 
ex3 = f'n = {n}, s = {text}, sum={x + y}'
print(ex3)

# 구분기호
m = 100000000

print(f'm : {m:,}')


# 정렬      ^ : 가운데 , < : 왼쪽 , > : 오른쪽

t = 20

print(f"t center : {t:10}")
print(f"t center : {t:^10}")
print(f"t center : {t:<10}")
print(f"t center : {t:>10}")

print(f"t center : {t:-^10}")
"""

#


    
