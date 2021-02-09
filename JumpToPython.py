1+2
# 3
3 / 2.4
# 1.25
3*9
# 27
a = 1
b = 2
a+b
a-b
a*b
a**b
a % b
a/b
a//b
# 3  -1   2    1   1  0.5   0
a = "Python"
print(a)
# Pythong
a = 3
if a > 1:
    print("a is bigger than 1")
# a is bigger than 1
for a in [1, 2, 3]:
    print(a)
# 1;2;3


def add(a, b):
    return a+b


add(3, 5)
# 8

print("""
주석문이
여러 줄 이라면
이러한 방법을 사용하면
편리하다
""")
#
# 주석문이
# 여러 줄 이라면
# 이러한 방법을 사용하면
# 편리하다
#

# cmd 에서 파이썬 출력
print("C:\'Users\'allofdaniel -> cd c:\doit -> python hello.py")
#print("C:\'Users\'allofdaniel -> cd c:\doit -> python hello.py")

# 소수점 표현
a = 4.24E10
b = 4.24e-10
print(a, b)
# 42400000000.0 4.24e-10

# 8진수 16진수
a = 0o177
print(a)
# 127

b = 0x8ff
c = 0xABC
print(b, c)
# 2303 2748

# 따옴표 문법

print("\"Python is very easy.\" he says.")
# "Python is very easy." he says.
c = "Life is too short\nYou need python"
print(c * 3)
# Life is too short
# You need pythonLife is too short
# You need pythonLife is too short
# You need python
print(c[0], c[-0], c[0:4])
#       L    L       Life

# 문자열 응용
print("="*50)
print("My Program")
print("="*50)
# ==================================================
# My program
# ==================================================

# 문자열 포매팅
"I eat %d apples." % 3
#'I eat 3 apples.'

"I eat %s apples." % "five"
#'I eat five apples.'

number = 3
"I eat %d apples." % number
#'I eat 3 apples.'

# %s string문자열   %d integer 정수     %f floating 소수

# 공백
"%10s" % "hi"
#'        hi'
"%-10s.jane" % "hi"
#'hi        .jane'
"%0.4f" % 3.42134234
# '3.4213'

"I eat {0} apples".format(3)
#'I eat 3 apples'
"I eat {0} apples".format("three")
#'I eat three apples'
"I eat {0} apples for {1} days".format(number, "three")
#'I eat 3 apples for three days'
"I eat {number} apples for {day} days".format(number=10, day="three")
"I eat {0} apples for {day} days".format(10, day="three")
#'I eat 10 apples for three days'

# 정렬
"{0:<10}".format("hi")
# 'hi        ' 왼쪽정렬
"{0:>10}".format("hi")
# '        hi' 오른쪽 정렬
"{0:^10}".format("hi")
# '    hi    ' 가운데 정렬
"{0:=^10}".format("hi")
# '====hi====' 가운데 정렬

"{{괄호표현}}".format()
# '{괄호표현}'

# f문자열 포매팅
name = '김다니엘'
age = 25
f'나의 이름은 {name}입니다. 나이는 {age}입니다. 내년에 {age+1}이 됩니다.'
'나의 이름은 김다니엘입니다. 나이는 25입니다. 내년에 26이 됩니다.'

# dictionary 응용
d = {'name': '김다니엘', 'age': 25}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다. '
#'나의 이름은 김다니엘입니다. 나이는 25입니다. '

# 문자열 관련 함수
name.count('다')
# 1 숫자세기
name.find('니')
# 2 위치찾기
name.index('엘')
# 3 위치찾기
name.join('5252')
# '5김다니엘2김다니엘5김다니엘2' 사이사이 끼어넣기
eng = "Daniel"
eng.upper()
eng.lower()
#'DANIEL'   'daniel'
eng.lstrip()
eng.rstrip()
eng.strip()
# 왼쪽 공백제거 오른쪽 공백제거 모두공백제거
eng.replace('Da', 'KimDa')
# KinDaniel
a = "Life is short"
b = "a:b:c"
a.split()
b.split(":")
#['Life', 'is', 'short']
#['a', 'b', 'c']

a = [1, 2, 3, ['a', 'b', 'c']]
a[0]
# 1
a[-1][0]
# 'a'
a = [1, 2, 3]
b = [4, 5, 6]
a+b
# [1,2,3,4,5,6]
a*3
# [1,2,3,1,2,3,1,2,3]
len(a)
# 3
str(a[2])+"hi"
# '3hi' str없이 작성시 오류발생.
a[2] = 4
# [1,2,4]
del a[1]
# [1,3]
a.append(4)
# [1,3,4]
a.append([5, 6])
# [1,3,4,[5,6]]
a = [1, 4, 3, 2]
a.sort()
# [1,2,3,4]
a = ['a', 'c', 'b']
a.sort()
# ['a','b','c']
a.reverse()
# ['c','b','a']
a.index('a')
# 2
a.pop()
# ['c','b']
a.count('b')
# 1
a.extend(['d', 'e'])
# ['c','b','d','e']

##tuple 자료형 ##
t1 = (1, 2, 'a', 'b')
t1[0]
# 1
t1[1:]
# (2,'a','b')
t2 = (3, 4)
t1+t2
# (1,2,'a,'b',3,4)
t2*3
# (3,4,3,4,3,4)
len(t1)
# 4
## dictionary 자료형##
a = {1: 'a'}
a[2] = 'b'
#{1: 'a', 2: 'b'}
# 90p
