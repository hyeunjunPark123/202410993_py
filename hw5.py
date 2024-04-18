# -*- coding: utf-8 -*-
"""hw5

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11hi2jJ8keSaWR9WjV_5pzHTo2sFaZDJf
"""

#202410993 박현준
#정수 읽기

def read_single_digit(a):
  if a == 0:
    return '영'
  elif a == 1:
    return '일'
  elif a == 2:
    return '이'
  elif a == 3:
    return '삼'
  elif a == 4:
    return '사'
  elif a == 5:
    return '오'
  elif a == 6:
    return '육'
  elif a == 7:
    return '칠'
  elif a == 8:
    return '팔'
  elif a == 9:
    return '구'

def read_number(b):
  if b >= 1000 :
    return '재입력'
  else :
    n100 = b // 100
    b = b - (n100*100)
    n10 = b // 10
    b = b - (n10*10)
    n = b
    n100 = read_single_digit(n100)
    n10 = read_single_digit(n10)
    n = read_single_digit(n)
    number = f"{n100} {n10} {n}"
    return number

num = int(input("세 자리 정수 입력: "))
print(read_number(num))