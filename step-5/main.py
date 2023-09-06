"""
모듈
"""

# math 모듈 수학적인 계산
import math
import random

print("=" * 10, "math", "=" * 10)
print(math.sqrt(2))  # 2의 제곱근
print(math.sqrt(3))  # 3의 제곱근
print(math.sqrt(4))  # 4의 제곱근
print(math.pi)  # 원주율
print()

# calendar
import calendar

print("=" * 10, "calendar", "=" * 10)
calendar.prmonth(2023, 9)
print()

# os
import os

print("=" * 10, "os", "=" * 10)
print(os.listdir())
print(os.getcwd())
print()

# 정규식
import re, glob

print("=" * 10, "re, glob", "=" * 10)
p = re.compile('.*p.*n.*')
for i in glob.glob('*'):
    m = p.match(i)
    if m:
        print(m.group())
print()

# webbrowser
import webbrowser

url = 'http://www.python.org/'
# webbrowser.open(url)

# random
print(random.randrange(1,7))
abc = ['a', 'b', 'c', 'd', 'e']
random.shuffle(abc)
print(abc)
print(random.choice(abc))