'''
제어구조
'''

# while
print("=" * 10, "while", "=" * 10)
a = 1
while a <= 10:
    print("a:::", a)
    a += 1
print()

# if-elif-else
a = 1234 * 4
b = 123456 / 2

print("=" * 10, "if-elif-else", "=" * 10)
if a > b:
    print('a > b')
elif a == b:
    print('a == b')
else:
    print('a < b')
print()

# for
print("=" * 10, "for", "=" * 10)
family = ['mother', 'father', 'gentleman', 'sexy lady']
for x in family:
    print(x, len(x))
print()

# match case switch와 비슷하지만 조건문 설정가능 하지만 파이썬 3.10부터 구현가능

# for-else
print("=" * 10, "for-else", "=" * 10)
for n in range(1, 11):
    print(n)
else:
    print('for end')
print()

# while-else
print("=" * 10, "while-else", "=" * 10)
n = 1
while n < 10:
    print(n)
    n += 1
else:
    print('while end')
print()


# tip
## and
print("=" * 10, "and", "=" * 10)
if a > 10 and a + b < 100:
    print('true')
else:
    print('false')
print()

## or
print("=" * 10, "or", "=" * 10)
if a > 10 or a - b < 100:
    print('true')
else:
    print('false')
print()

## in
print("=" * 10, "in", "=" * 10)
text = 'banana'
if 'a' in text:
    print('true')
else:
    print('false')
print()

## lower()
print("=" * 10, "lower()", "=" * 10)
text2 = 'Test'
print(text2.lower())
print(text2)
print(text2[1])
print()

## upper()
print("=" * 10, "upper()", "=" * 10)
print(text2.upper())
print()

## range()
print("=" * 10, "range()", "=" * 10)
for x in range(2, 10):
    print(x)
print()
