import pandas as pd
import os
import threading
import sys

#계산 하는 함수
def Calc():
    # 7hz 초기값 평균
    a = Fp1_FFT.loc[0:1, '6.50Hz':'7.50Hz']
    sum7_initial = 0

    for i in range(0, 1):
        for j in range(0, 30):
            sum7_initial = sum7_initial + a.iloc[i, j]
    avg7_initial = sum7_initial / 30
    print("7hz의 초기 평균값" + avg7_initial)  # 엑셀 파일에서 결괏값 1.10279E-11

    # 13hz 초기값 평균
    b = Fp1_FFT.loc[0:1, '12.50Hz':'13.50Hz']
    sum13_initial = 0
    for i in range(0, 1):
        for j in range(0, 30):
            sum13_initial = sum13_initial + b.iloc[i, j]
    avg13_initial = sum13_initial / 30
    print("13hz 초기 평균값" + avg13_initial)  # 엑셀 파일에서 결괏값 4.06134E-12

    # 7hz 자극 후 평균
    c = Fp1_FFT.loc[2:3, '6.50Hz':'7.50Hz']  # 자극 후 범위 다시 지정해야함
    sum7_after = 0
    for i in range(0, 1):
        for j in range(0, 30):
            sum7_after = sum7_after + c.iloc[i, j]
    avg7_after = sum7_after / 30
    print("7hz 자극후 평균값: "+ avg7_after)

    # 13hz 자극 후 평균
    d = Fp1_FFT.loc[2:3, '12.50Hz':'13.50Hz']  # 자극 후 범위 다시 지정해야함
    d
    sum13_after = 0
    for i in range(0, 1):
        for j in range(0, 30):
            sum13_after = sum13_after + d.iloc[i, j]
    avg13_after = sum13_after / 30
    print("13hz 자극후 평균값: " + avg13_after)

    # 차잇값 구하기
    diff7 = avg7_after - avg7_initial
    diff13 = avg13_after - avg13_initial
    print(diff7)
    print(diff13)

    # 차잇값에 따른 결과 처리
    # 결과 처리(텍스트 파일 띄우기)
    if (sum7_initial < sum7_after and sum13_initial > sum13_after):
        f = open('./Web/result.txt', 'w')
        f.write('7hz')
        f.close

    elif (sum7_initial > sum7_after and sum13_initial < sum13_after):
        f = open('./Web/result.txt', 'w')
        f.write('13hz')
        f.close

    else:  # 둘 다 오르거나 떨어진 경우
        if (diff7 > diff13):
            f = open('./Web/result.txt', 'w')
            f.write('7hz')
            f.close
        elif (diff7 < diff13):
            f = open('./Web/result.txt', 'w')
            f.write('13hz')
            f.close


#정답 텍스트 파일 생성 함수
def AnswerData(answer):
    f = open("./Web/result.txt", 'w')
    if answer == "7hz":
        data = "7hz"
    elif answer == "13hz":
        data = "13hz"
    f.write(data)
    f.close()

#파이썬 메인 파일 시작
# 파일 경로로 접근해서 파일 열기
path = '/Users/nadonghyeon/NeuroFocusData/Mave/'

file_list = os.listdir(path)
print(file_list)

real_path = path + file_list[2] + "/"
file_list2 = os.listdir(path + file_list[2])

print(file_list2[1])

file = real_path + file_list2[1]
print(file)

#엑셀 읽기
Fp1_FFT = pd.read_csv(file, delimiter='\t', encoding='cp949')

#현재 경로
# /Users/nadonghyeon/NeuroFocusData/Mave/2022-06-11_오후 3_56/Fp2_FFT.txt

#자극 시작 시점(행)
startPoint = len(Fp1_FFT)

# 노이즈 값 끝 시점(행)
dumpEndPoint = len(Fp1_FFT) + 35

# 초기값 끝 시점(행)
initialTimeEndPoint = dumpEndPoint + 10

# 종료 시점(행)
TotalEndPoint = initialTimeEndPoint + 25

#일정 시간 기다림
threading.Timer(80, Calc()).start()
sys.exit(0)






