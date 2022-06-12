import pandas as pd
import os
import threading
from time import sleep
import sys

#계산 하는 함수
def cal(dumpEndPoint, initialTimeEndPoint, TotalEndPoint):
    # 7hz 초기값 평균
    Fp1_FFT = pd.read_table(file, sep='\t', encoding='cp949', float_precision='high')
    a = Fp1_FFT.loc[dumpEndPoint:initialTimeEndPoint, '6.50Hz':'7.50Hz']

    print("판다스 사이즈 개수")
    print(a.size)
    print("판다스 행과열의 개수")
    print(a.shape)
    sum7_initial = 0
    print("행 개수")
    print(initialTimeEndPoint - dumpEndPoint)
    print("열 개수")
    print(TotalEndPoint - (initialTimeEndPoint + 1))
    for i in range(0, initialTimeEndPoint - dumpEndPoint):
        for j in range(0, 30):
            sum7_initial = sum7_initial + a.iloc[i, j]
    avg7_initial = sum7_initial / ((initialTimeEndPoint - dumpEndPoint) * 30)
    print("초기값의 개수")
    print((initialTimeEndPoint - dumpEndPoint) * 30)
    print("7의 초기값")
    print(avg7_initial)

    # 13hz 초기값 평균
    Fp1_FFT = pd.read_table(file, sep='\t', encoding='cp949', float_precision='high')
    b = Fp1_FFT.loc[dumpEndPoint:initialTimeEndPoint, '12.50Hz':'13.50Hz']
    sum13_initial = 0
    for i in range(0, initialTimeEndPoint - dumpEndPoint):
        for j in range(0, 30):
            sum13_initial = sum13_initial + b.iloc[i, j]
    avg13_initial = sum13_initial / ((initialTimeEndPoint - dumpEndPoint) * 30)
    print("13의 초기값")
    print(avg13_initial)

    # 7hz 자극 후 평균
    Fp1_FFT = pd.read_table(file, sep='\t', encoding='cp949', float_precision='high')
    c = Fp1_FFT.loc[initialTimeEndPoint + 1:TotalEndPoint, '6.50Hz':'7.50Hz']
    sum7_after = 0
    for i in range(0, TotalEndPoint - (initialTimeEndPoint + 1)):
        for j in range(0, 30):
            sum7_after = sum7_after + c.iloc[i, j]
    avg7_after = sum7_after / ((TotalEndPoint - (initialTimeEndPoint + 1)) * 30)
    print("7의 자극후값")
    print(avg7_after)

    # 13hz 자극 후 평균
    Fp1_FFT = pd.read_table(file, sep='\t', encoding='cp949', float_precision='high')
    d = Fp1_FFT.loc[initialTimeEndPoint + 1:TotalEndPoint, '12.50Hz':'13.50Hz']
    sum13_after = 0
    for i in range(0, TotalEndPoint - (initialTimeEndPoint + 1)):
        for j in range(0, 30):
            sum13_after = sum13_after + d.iloc[i, j]
    avg13_after = sum13_after / ((TotalEndPoint - (initialTimeEndPoint + 1)) * 30)
    print("13의 자극후값")
    print(avg13_after)

    # 차잇값 구하기
    diff7 = avg7_after - avg7_initial
    diff13 = avg13_after - avg13_initial
    print("7의 차이값")
    print(diff7)
    print("13의 차이값")
    print(diff13)

    # 차잇값에 따른 결과 처리
    # 결과 처리(텍스트 파일 띄우기)
    if (avg7_initial < avg13_after and avg13_initial > avg13_after):
        f = open('../Web/Pages/result.txt', 'w')
        print("7들어옴")
        f.write('7hz')
        f.close

    elif (avg7_initial > avg13_after and avg13_initial < avg13_after):
        f = open('../Web/Pages/result.txt', 'w')
        print("13들어옴")
        f.write('13hz')
        f.close

    else:  # 둘 다 오르거나 떨어진 경우
        print("둘다 오르는경우나 떨어진 경우들어옴")
        if (diff7 > diff13):
            print("둘7들어옴")
            f = open('../Web/Pages/result.txt', 'w')
            f.write('7hz')
            f.close
        elif (diff7 < diff13):
            print("둘13들어옴")
            f = open('../Web/Pages/result.txt', 'w')
            f.write('13hz')
            f.close


#파이썬 메인 파일 시작

#웹상에서 뇌파 분석하기 버튼을 클릭할때부터 파이썬 파일이 열리는데 바로 분석하면 데이터가 차마 들어오지 못하니 측정시간 1분 10초에 10초를 더한 80초후에 메인 파일이 실행 되게함


# 파일 경로로 접근해서 파일 열기
path ='C:/MAVE_RawData/'

file_list = os.listdir(path)
#폴더내 파일 개수 세기
number_files = len(file_list)
print(number_files)
set_index = number_files - 1

real_path = path + file_list[set_index] + "/"
print(real_path)

file_list2 = os.listdir(path + file_list[set_index])
print(file_list2[1])

file = real_path + file_list2[1]
print(file)

#현재 경로(맥)
# /Users/nadonghyeon/NeuroFocusData/Mave/2022-06-11_오후 3_56/Fp2_FFT.txt
#윈도우
#C:/MAVE_RawData/2022-06-11_오후 3_56/Fp1_FFT.txt

#파이썬 경로 읽기
Fp1_FFT = pd.read_table(file, sep='\t', encoding='cp949', float_precision='high')

#실제 자극 시작 시점(행)
startPoint = len(Fp1_FFT) - 2
#startPoint = 73

print("시작점")
print(startPoint)

# 노이즈 값 끝 시점(행) (초기값 계산 측정 시점)
dumpEndPoint = startPoint + 35
#dumpEndPoint = startPoint + 3
print("초기값 계산 측정")
print(dumpEndPoint)

# 초기값 끝 시점(행) (초기값 계산 측정 종료 시점)(자극값 계산 측정 시점)
initialTimeEndPoint = dumpEndPoint + 10
print("자극값 계산 시점")
print(initialTimeEndPoint)

# 종료 시점(행) (자극값 종료 시점)
# TotalEndPoint = initialTimeEndPoint + 25
TotalEndPoint = initialTimeEndPoint + 25
print("자극값 종료")
print(TotalEndPoint)

#계산 기다림
sleep(75)

#일정 시간 기다림 (로딩중일 때 까지 기다림)
# threading.Timer(80, cal(dumpEndPoint,initialTimeEndPoint,TotalEndPoint)).start()
print("초기값 계산 측정2")
print(dumpEndPoint)
print("자극값 계산 시점2")
print(initialTimeEndPoint)
print("자극값 종료2")
print(TotalEndPoint)
cal(dumpEndPoint, initialTimeEndPoint, TotalEndPoint)
# sys.exit("뇌파 분석을 종료합니다.")
# os.system('pause')

