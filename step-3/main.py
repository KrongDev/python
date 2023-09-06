"""
함수
"""
from functools import reduce

# 함수
print("=" * 10, "def", "=" * 10)


def print_list(a):
    for i in a:
        print(i)


print_list([1, 2, 3, 4])
print()

# 예시 문제


## 양의 정수를 입력받아, 그 수가 몇 자리 숫자인지 출력하는 함수 numOfDigits()를 만들어보세요
print("=" * 10, "numOfDigits", "=" * 10)


def numOfDigits(num):
    return len(str(num))


print(numOfDigits(123))
print()

## 곱하기
print("=" * 10, "multi", "=" * 10)


def multi(m):
    for n in range(1, 11):
        print(f"{m} * {n} = {m * n:2d}")


multi(3)
print()

# 반환문 함수
print("=" * 10, "return def", "=" * 10)


def f1(x):
    a = 3
    b = 5
    y = a * x + b
    return y


c = f1(10)
print(c)
print()

# 람다 표현 식
print("=" * 10, "lambda", "=" * 10)
a = (lambda x, y: x + y)
print(a(10, 20))
print()

# map()
print("=" * 10, "map", "=" * 10)
print(map(lambda x: x ** 2, range(5)))
print(list(map(lambda x: x ** 2, range(5))))
print()

# reduce()
print("=" * 10, "reduce", "=" * 10)
print(reduce(lambda x, y: x + y, [0, 1, 2, 3, 4]))
print(reduce(lambda x, y: y + x, 'abcd'))
print()

# filter()
print("=" * 10, "filter", "=" * 10)
print(list(filter(lambda x: x % 2 == 0, range(10))))
print()
