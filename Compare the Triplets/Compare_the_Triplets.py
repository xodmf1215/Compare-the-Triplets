
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    a_score = 0
    b_score = 0
    result=[0,0]
    if a[0] > b[0]:
        a_score += 1
    elif a[0] < b[0]:
        b_score += 1
    if a[1] > b[1]:
        a_score += 1
    elif a[1] < b[1]:
        b_score += 1
    if a[2] > b[2]:
        a_score += 1
    elif a[2] < b[2]:
        b_score += 1
    result[0] = a_score
    result[1] = b_score
    return result
if __name__ == '__main__':
    filename = os.path.join("C:",os.sep,"Users","user","Downloads","output.txt") #os.path를 통해 linux등 os 환경에 맞는 경로 string 생성
    fptr = open(filename, 'w')
    a = list(map(int, input().rstrip().split())) 
        #list는 list 객체 생성문
        #map 은 지정한 함수로 list, dictionary 처럼 반복되는 인자를 전달해 list 형태로 반환
        #input으로 line 입력, rstrip은 문자열 가장 오른쪽에 있는 공백들을 지우는 것, split()은 공백(탭,엔터,스페이스)를 기준으로 문자열 나누기, split(":")은 : 를 기준으로 문자열나누기 

    b = list(map(int, input().rstrip().split()))

    result = solve(a, b)

    fptr.write(' '.join(map(str, result)))
        #string객체에서 .join을 쓰면 join에 포함된 리스트 내용들을 string 객체를 통해 결합
    fptr.write('\n')

    fptr.close()