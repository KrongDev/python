'''
파이썬 기본 사용법!!
'''
import math

# 덧셈
a = 1 + 2
print("덧셈:::" + str(a))

# 뺄셈
b = 10 - 2
print("뺄셈:::" + str(b))

# 곱셈
c = 10 * 2
print("곱셈:::" + str(c))

# 나눗셈
d = 10 / 3
print("나눗셈:::" + str(d))

# 소숫점 없는 나눗셈
da = 10//3
print("소숫점 없는 나눗셈:::" + str(da))

# 나머지
e = 10 % 2
print("나머지:::" + str(e))

# 몫과 나머지를 한번에 구하기
f = divmod(10, 2)
print("몫과 나머지를 한번에 구하기:::" + str(f))

# 루트
g = math.sqrt(4)
print("루트:::" + str(g))

# 제곱
h = 5 ** 5
print("제곱:::" + str(h))

# 리스트
i = ['a', 'b', 'c']
print("리스트:::" + str(i))

# 리스트 길이 체크 - len()
print("리스트 길이체크:::" + str(len(i)))

# 리스트 index로 값 출력
print("리스트 index로 값 출력:::" + i[2])

# 리스트 값 삭제 - remove
i.remove('a')
print("리스트 a를 뺸 값 출력:::" + str(i))

# tip

## round() 소숫점 반올림
## 1번째 인자 : 값
## 2번째 인자 : 명시하는 소숫점 자리로 반올림
ex1 = round(1.2345, 2)
print('소숫점 반올림 - round():::', ex1)
