"""
파일을 다뤄보자

절대 주소: C:/Users/.../step-5/Python_for_Fun.txt
상대 주소: ./Python_for_Fun.txt

open(파일주소, 상태)

상태 종류
w : 새파일 열어 글쓰기
a+: 추가해서 글쓰기
wb: byte 파일 열기
rb: byte 파일 읽기
"""
f = open('./Python_for_Fun.txt')
print(f.read())
print("=" * 50)
# letter = open('./letter.txt', 'w')
# letter.write('Hello')
# letter.close()
#
# text_write = open('./Python_for_Fun.txt', 'a+')
# text_write.write('\nHello')
# text_write.close()

f = open('./Python_for_Fun.txt')
print(f.readline())
print("=" * 50)
lines = f.readlines()
print(lines)
print("=" * 50)

# users = {'kim':'3kid9', 'sun80':'393948', 'ljm':'py90390'}
# f = open('users', 'wb')
import pickle
# pickle.dump(users, f)
# f.close()
f = open('users', 'rb')
a = pickle.load(f)
print(a)
print("=" * 50)

from glob import glob

print(glob('*txt'))