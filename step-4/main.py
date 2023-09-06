"""
데이터 타입
"""

# 자료형
print("=" * 10, "data type", "=" * 10)
a = 10
b = '10'
c = [1, 2, 3, 4, 5]
d = ('a', 'b', 'c', 'd')
e = {'one': 1, 'two': 2, 'three': 3}
f = False
g = {1, 2, 3, 4, 5}
print(f"b의 타입은 : {type(a)}")
print(f"b의 타입은 : {type(b)}")
print(f"c의 타입은 : {type(c)}")
print(f"d의 타입은 : {type(d)}")
print(f"e의 타입은 : {type(e)}")
print(f"f의 타입은 : {type(f)}")
print(f"g의 타입은 : {type(g)}")

## complex = 복소수
print(type(3 + 4j))
print()

# 문자열
print("=" * 10, "str", "=" * 10)
x = 'banana'
print(x[0])
print(x[2:4])  # 2, 3
print(x[:3])  # 0, 1, 2, 3
print(x[3:])  # 3, 4, ...

## 문자열에 어떤 글자가 몇 번째 자리에 있는지 알고 싶을 때
print(x.find('n'))
y = ' testtest '
print(y.lstrip())
print(x.split('a'))
print()

# 리스트
print("=" * 10, "list", "=" * 10)
prime = [3, 7, 11]
prime.append(5)
print(prime)
prime.sort()
print(prime)
prime.insert(0, 2)
print(prime)
del prime[4]
print(prime)
a = prime.pop()
print(a)
print(prime)
prime[0] = 1
print(prime)
orders = [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
print(orders[1])
print(orders[1][2:])
## 문자열을 리스트로
characters = []
sentence = 'Be happy!'
for char in sentence:
    characters.append(char)
print(characters)
print(list('Be happy2!'))
## sum()
one_to_ten = list(range(1, 11))
print(sum(one_to_ten))
print()

# tuple
print("=" * 10, "tuple", "=" * 10)


def magu_print(x, y, *rest):
    print(x, y, rest)


magu_print(1, 2, 3, 4, 5, 6, 7, 8, 9)
one = 5,
print(one)
p = (1, 2, 3)
q = list(p)
print(q)
r = tuple(q)
print(r)
print()

# dict
print("=" * 10, "dict", "=" * 10)
family = {'mom': 'Kim', 'dad': 'Choi', 'baby': 'Choi'}
print(family)
print(family.keys())
print(family.values())
print(family.items())
print('dad' in family)
print()

# set
print("=" * 10, "set", "=" * 10)
fruits = {'apple', 'banana', 'orange'}
fruits.add('mango')
print(fruits)
companies = {'apple', 'microsoft', 'google'}
print(fruits & companies)
print(fruits | companies)
list_of_sets = [fruits, companies]
print(list_of_sets)
print(set.intersection(*list_of_sets))
print(set.union(*list_of_sets))
alphabet = list('google')
print(set(alphabet))
s1 = {1, 2, 3, 4, 5, 6, 7}
s2 = {3, 6, 9}
print(s1 - s2)
