print('hellow')
import keyword
print(keyword.kwlist)
print()
print("hi")
print(type("안녕"))
print("\'안녕하세요\"라고말했습니다")
print("안녕하세요\n반갑습니다\t하이")
print("안녕하세요"[0])
len("안녕하세요")
print("5/3=",3//5)
print("5%3=",5%3)
print("2**2=",2**2)
pi=3.14159265358979
r=10
print(2*pi*r)
print(pi*r**2)
number=100
number+=10
number%=3
string="안녕"
string+="!"
string*=3
string*=3
string
#input("인사말을 입력하세요>")
#string=input("인사말을 입력하세요>")
#print(type(string))
#string=int(string)
#type(string)
"{}".format(10)
string = "{} {}".format(10,20)
string = print("{}만원".format(5000))
string = "{:500d}".format(5000)
string = "{:05d}".format(5000)
print("#기본")
string = "{: d}".format(40)
string = "{:+d}".format(-40)
print("{:=+05d}".format(42))
print("{:+015f}".format(52.283))
b= "hellow wolrd"
print(b.upper())
print("Hi".upper())
print("{:g}".format(52.500))
c = """ 
안녕하세요
공부중 입니다.
"""
print(c.strip())
print(c.isalpha())
print("안녕안녕하세요".find("안녕"))
print("안녕안녕하세요".rfind("안녕"))
print("안녕하세요" in "안녕하세요반가워요")
print("1 2 3 4 5   9".split())
print("1"=="2")
print("1"!="2")
print(not True)
print(True and False)
print(True or False)
string=3
if string>1 : 
    print("정말 True입니다")
    print("찐입니다")
import datetime
now = datetime.datetime.now()
print(now.year)
print(now.day)
print(now.second)
print("{}년{}월{}일 오후{}시{}분{}초".format(now.year,now.month,now.day,now.hour-12,now.minute,now.second))
number=input("정수입력??")
number_last=number[-1]
number=int(number)
type(number)
if number%2 == 0:
    print("짝수입니다")
if number%2 == 1:
    print("홀수입니다")
raise NotImplementedError
pass
list_a=[1,2,3]
list_b=[4,5,6]
list_a+list_b
list_a*3
list_a.append("b")
list_a
list_a.insert(3,c)
list_a.extend([0,0,0])
list_a
list_a.pop(3)
del list_a[3]
'b' in list_a
'3' not in list_a
array = [273,32,103,52,23]
for element in array:
    print(element)
dict_a = {
    "name":"어벤져스 앤드게임",
    "type":"히어로무비",
    "director":["안소니 루소","조 루소"]
}
dict_a["name"]
dict_a["type"]
dict_a["director"]
dict_a["money"]=5000
del dict_a["money"]
dict_a

list(range(0,10+1,2))
list(range(0,11//2))

array = [276,32,103,57,52]

for i in range(len(array)):
    print("{}번째 반복 : {}".format(i, array[i]))

for i in range(5,-1,-1):
    print("{}번째 반복".format(i))

for i in reversed(range(5)):
    print("{}번째 반복".format(i))

#while True:
 #   print(".",end="")

while i<10:
    print("{}번째 반복".format(i))
    i+=1

list_test=[1,2,1,2,1,2]
while 2 in list_test:
    list_test.remove(2)
print(list_test)

import time
number = 0
target_tick==time.tick()+5
while time.time() < target_tick:
    number +=1 

print("5초동안 {}번 반복했습니다.".format(number))

while True:
    print("{}번째 반복입니다.".format(number))
    number += 1
    input_text =input("종료하시겠습니끼(y): ")
    if input_text in ["y","Y"]:
    print("종료되었습니다.")
    break

array = [5,1,16,583,20,15]
for number in array:
    if number < 10:
        continue
    print(number)

min(20,11,8)
min(array)
print("{}는 최소숫자입니다.".format(min(array)))
max(array)
sum(array)

reversed(array)
array[::-1]

example_dictionary = { "키A":"값A", "키B":"값B", "키C":"값C"}
print(example_dictionary.items())
for key,element in example_dictionary.items():
    print("키{}:값{}"example_dictionary.items(key,element))

array=[]
for i in array(0,20,2):
    array.append(i*i)
print(array)

array=[i*i for i in range(0,20,2)]

array=["사과","배","포도","귤"]
output = [fruit for fruit in array if fruit !="귤"]
print(output)

number = int(input("정수 입력> "))
if number %2 == 0:
    print("""\ 
    입력한 문자열은 {}입니다. 
    {}는(은) 짝수입니다.""".format(number,number))
else : 
    print("""\ 
    입력한 문자열은 {}입니다. 
    {}는(은) 홀수입니다.""".format(number,number))
    
number = int(input("정수 입력> "))
if number %2 ==0:
    print("입력한 문자열은 {}입니다.\n{}는 짝수입니다.".format(number,number))
else:
    print("입력한 문자열은 {}입니다.\n{}는 홀수입니다.".format(number,number))

test = (
    "이렇게"
    "입력해도"
    "하나의 문자열로 연결되어"
    "생성 됩니다."
)
print("test:", test)
print(type(test))

print("::".join(["1","2","3","4","5"]))

numbers = [1,2,3,4,5]
r_num = reversed(numbers)
print(next(r_num))
print(next(r_num))

def print_3_times():
    print(input("3번반복합니다>"))*3

print_3_times()

def print_n_times(value, n):
    for i in range(n):
    print(value)

print_n_times("ㅎㅇ",5)

def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= 1
    return output

def factorial(n):
    if n ==0:
        return 1
    else :
        return n*factorial(n-1)

def fibonacci(n):
    if n =< 2:
        return 1
    else:
        return n+n-1
