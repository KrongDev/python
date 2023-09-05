'''
terminal 에서 해당 파일 위치로 이동 한 후 'python triangle.py' 입력하면 호출

가능한 이유 : 파이썬이 컴퓨터에서 바로 읽는 인터프리터 방식의 언어이기 때문

참고) 자바는 컴퓨터가 이해하기 위해 컴파일러가 필요하다
'''

print('직각삼각형 그리기\n')
leg = int(input('변의 길이: '))

for i in range(leg):
    print('* ' * (i + 1))

area = (leg ** 2) / 2
print('넓이:', area)
