#파이썬 리스트
#자료구조에서 중요
#리스트 자료형(순서o, 중복o, 수정o, 삭제o)

#선언
a = []
b = list()
c = [70, 75, 80, 85] #len
d = [1000, 10000, 'ace', 'Base', 'Captine']
e = [1000, 10000, ['ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

#인덱싱 
print('>>>>>')
print('d - ', type(d),d)
print('d -', d[1])
print('d -', d[0] + d[1] + d[1])
print('d -',d[-1])
print('e - ',e[-1][1])
print('e - ',list(e[-1][1])) #형 변환

#슬라이싱
print('>>>>>>>')
print('d -', d[0:3])
print('d -', d[2:])
print('e -', e[-1][1:3])

#리스트 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))

#값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

# Identity(id)

temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('>>>>>>')
c[0] = 4
print('c -', c)
c[1:2] = ['a', 'b', 'c']
print('c -', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)