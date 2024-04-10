"""
str1 = 'I am Python'
str2 = "Python"
str3 = "How are you?"
str4 = 'Thank you!'

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈문자열 
str1_t1 = ''
str2_t2 = str()
print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

#이스케이프 문자 사용
#I'm Boy
print("I'm Boy")
print('I\\m Boy')
print('a \t b')
print('a \" \" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New line \n Check!"

print(t_s1)
print(t_s2)

# Raw String
raw_s = r'D:\python\test'

print(raw_s)

#멀티라인 입력
multi_str = \
'''
string
Multi line
Test
'''
print(multi_str)

#문자열 연산
str_o1 = 'python'
str_o2 = 'Apple'
str_o3 = 'How are you doing'
str_o4 = 'Seoul Deajeon Busan Jinju'

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('p' in str_o1)
print('p' not in str_o2)


# 문자열 형 변환
print(str(66),type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))


#문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)

print("Capitalize: ", str_o1.capitalize()) # 첫번째 문자를 대문자로 바꿈
print('endswith:', str_o2.endswith('e')) # 마지막 문자가 e로 끝나는지
print('replace:', str_o1.replace("thon", "good")) #문자 바꾸기
print('sorted:', sorted(str_o1)) #문자를 정렬해서 리스트형태로 나오게 하기
print('split:', str_o4.split(' ')) #특정문자를 지정하면 그곳부터 나누어짐

#반복(시퀀스)
im_str = 'Good Boy!'

print(dir(im_str)) #___iter___
#출력
for i in im_str:
    print(i)


#슬라이싱 연습
str_sl = "Nice Python"


#슬라이싱 연습
print(str_sl[0:3])  # 0 1 2
print(str_sl[5:11]) #[5:11]
print(str_sl[:len(str_sl)]) # str_sl[:11] len은 길이를 뜻하는 함수로 끝부분 체크
print(str_sl[:len(str_sl)-1]) #str_sl[:10]
print(str_sl[1:9:2])
print(str_sl[-5:])
print(str_sl[1:-2])  
print(str_sl[::-1])  # 뒤집힘
print(str_sl[::2])
"""
# 아스키 코드
a = 'z'

print(ord(a)) # 아스키 코드로
print(chr(122)) # 문자로

#확인용 코드


