"""
예외 처리
"""

def f(a,b):
    try:
        if a and b:
            return (a*b) + (a/b)
        elif a:
            return '불능'
        else:
            return '부정'
    except:
        return '제대로 입력해주세요'


print(f(3, '53w5'))