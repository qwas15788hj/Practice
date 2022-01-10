# input은 return이 있다.
# name = input("이름을 입력해주세요.") 
# print("안녕하세요", name)

# text = input('날짜 입력 yyy.mm.dd')
# y,m,d = text.split('.')

# print(text, y, m, d)
# print(type(y))
# print(type(text))

# split(): ()기준으로 자르기 , map(a, b): b를 a로
# a,b,c = map(int,input('a b c값 입력').split())
# print(a,b,c, a+b+c)

# 줄
# x = 3
# y = 5
# print('{}과 {}의 합은 {}이다.'.format(x,y,x+y))

# 반올림: round, 절대값: abs(a), 제곱:pow(a,b), 나눗셈:divmod(a,b)
# print(round(3.33))
# print(abs(-3))
# print(pow(3,2))
# x,y = divmod(7,2)
# print(sum([7,5,1,3]))

# print(text[::-1]) : 문자열 뒤집기

# if ~elif ~else

# while 문
# text=input('e 또는 E 입력 시 종료')

# while text!='e' and text!='E':
#     text=input('e 또는 E 입력 시 종료')

# print("종료")

# for 문
# a에서 b까지 출력
# a, b = map(int,input('a b:').split())
# for i in range(a, b+1):
#     print(i)

# # list li=list[]
# # 추가하기
# li = ['a', 'b', 'c'] 
# li.append('f')
# li.insert(0,'aa')
# # 삭제하기
# li.remove('aa')
# del li[2]
# 정렬
# num=[1,2,3,4,7,6,8]
# num.sort()   :오름차순 정렬
# num.sort(reverse=True)  :내림차순 정렬

# # 튜플 tu=tuple()
# num = (5,7,9)
# n1,n2,n3 = num  # 변수할당

# a = 'hello'
# b = 'world'
# (a,b) = (b,a) # 값 교환하기

# 세트 se=set()
# a={1,2,3}
# b={2,3,4}
# a&b
# a|b
# a-b
# a^b

# # 딕셔너리 dic=dict()
# dic={'kor':80, 'eng':90, 'mat':77}
# dic.keys() # 모든 키 얻기
# dic.values() # 모든 값 얻기
# dic.items # 모든 순서쌍 얻기

# # 리스트의 활용
# li = list(map(int,input('숫자입력').split()))

# *함수*
# def aa():
#     print("hi~")
    
# def bb(x):
#     for i in range(x):
#         print("hello~")
        
# def cc():
#     n=int(input('n:'))
#     print(n*2)
#     return n*2

# def dd(x,y):
#     print(x*y)
#     return x*y

# re1 = aa()
# re2 = bb(3)
# re3 = cc()
# re4 = dd(3,5)

# 내장모듈
# import math
# import random
# print(random.randint(1,5))

# 체크하기
# li = list(map(int, input('li:').split()))
# n = int(input('n:'))

# check = False

# for i in li:
#     if i == n:
#         check = True
# print(check)
# 위랑 같음
# print(n in li)

# # 약수의 개수 구하기
# n = int(input('n:'))
# li = []

# for i in range(1, n+1):
#     if n%i==0:
#         li.append(i)
# print(len(li))

# # OX개수 구하기
# text = list(input('text:'))
# print(text.count('o'))
# print(text.count('x'))

# # 평균 이상 개수 구하기
# num = list(map(int,input('num:').split()))
# avg = sum(num)/len(num)

# check = 0

# for i in num:
#     if i>=avg:
#         check = check+1
# print(avg)
# print(check)

# # 소수 판별하기
# num = int(input('num:'))
# check=0
# for i in range(1, num+1):
#     if num%i == 0:
#         check=check+1
        
# if check == 2:
#     print("소수입니다")
# else:
#     print("소수가 아닙니다")

# # 범위 내의 소수 구하기
# a = int(input('a:'))
# li = []

# for n in range(2, a+1):
#     check = True
#     for i in range(2,n):
#         if n%i == 0:
#             check = False
#     if check:
#         li.append(n)
        
# print(li)

# # 등비 수열
# n = int(input('n:'))
# a = int(input('a:'))
# r = int(input('r:'))

# for i in range(n-1):
#     a=a*r
# print(a)

# # 피보나치 수열
# n=int(input('n:'))
# a=1
# b=1

# for i in range(n-2):
#     c=a+b
#     a=b
#     b=c
# print(b)

# 별찍기
# 계단
# n=int(input('n:'))
# for i in range(n):
#     print(' '*i,end='')
#     print('*'*n)

# # 역삼각형
# n=int(input('n:'))

# for i in range(n):
#     print(' '*i,end='')
#     print('*'*(n-i))

# # 피라미드
# n = int(input('n:'))
# for i in range(n):
#     print(' '*(n-i-1),end='')
#     print('*'*(i*2+1))

# # 주사위
# a=int(input('a:'))
# b=int(input('b:'))
# n=int(input('n:'))

# for i in range(1, a+1):
#     for j in range(1, b+1):
#         if i+j == n:
#             print(i,j)

# # 구구단
# for i in range(2, 10):
#     for j in range(1, 10):
#         print('{}*{}={}'.format(i,j,i*j))
#     print()

# # 행렬 만들기
# li = [[1,2,3,4],[5,6,7,8]]

# for i in range(len(li)):
#     for j in range(len(li[i])):
#         print(li[i][j],end='')
#     print()

# # 띄어쓰기 없애기
# text = input('text')
# for i in text:
#     if i != ' ':
#         print(i,end='')

# # 대소문자 바꾸어 출력하기
# text = input('text')
# for i in text:
#     if i.isupper():
#         print(i.lower(),end='')
#     elif i.islower():
#         print(i.upper(),end='')
#     else:
#         print(i, end='')

# # 이름 찾기
# name=['김철수','김영희','홍길동','이소울','최코딩']
# for i in name:
#     if '철' in i:
#         print(i)

# for i in name:
#     if i[0] =='김':
#         print(i)

# # 최소값 구하기
# li=list(map(int,input('숫자 입력:').split()))
# print(li)
# print(min(li))
# print(type(li[2]))
# m = li[0]

# for i in li:
#     if i<m:
#         m=i
# print(m)

# # 최대값 구하기
# li=list(map(int,input('숫자 입력:').split()))

# m = li[0]

# for i in li:
#     if i>m:
#         m=i
# print(m)

# # 선형 탐색
# li = [1,6,4,2,3,10,8,7,5,9]
# n=int(input('1~10'))

# for i in range(len(li)):
#     if li[i] == n:
#         print("인덱스" + str(i) + "번째에 있습니다.")
#         break

# # 이진 탐색
# li = [1,5,6,8,9,17,13,15,19,3]
# li.sort()
# n=int(input('1,3,5,6,8,9,13,15,17,19: '))

# s_index = 0
# e_index = len(li)-1

# while s_index <= e_index:
#     m_index=(s_index+e_index)//2
#     if n < li[m_index]:
#         e_index = m_index-1
#     elif n > li[m_index]:
#         s_index = m_index+1
#     else:
#         print(m_index)
#         break

# # 선택 정렬
# li = [8,6,4,1,2,3,5,10,9,7]

# for i in range(len(li)):
#     print(li)
#     m_index = i
#     for j in range(i,len(li)):
#         if li[j] < li[m_index]:
#             m_index = j
#             print(m_index)
#     li[i], li[m_index] = li[m_index], li[i]

# # 버블 정렬
# li = [8,6,4,1,2,3,5,10,9,7]

# for i in range(len(li)):
#     print(li)
#     for j in range(len(li)-i-1):
#         if li[j] > li[j+1]:
#             li[j], li[j+1] = li[j+1], li[j]


s=[1,2,3]
print(s[-2])