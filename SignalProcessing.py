import pandas as pd
import os


#계산 하는 함수
def cal():
    # 7hz 초기값 평균
    a = Fp1_FFT.loc[33:43, '6.50Hz':'7.50Hz']
    a

    sum7_initial = 0
    for i in range(0, 10):
        for j in range(0, 30):
            sum7_initial = sum7_initial + a.iloc[i, j]
    avg7_initial = sum7_initial / 300
    print("7의 초기값")
    print(avg7_initial)

    # 13hz 초기값 평균
    b = Fp1_FFT.loc[33:43, '12.50Hz':'13.50Hz']
    b
    sum13_initial = 0
    for i in range(0, 10):
        for j in range(0, 30):
            sum13_initial = sum13_initial + b.iloc[i, j]
    avg13_initial = sum13_initial / 300
    print("13의 초기값")
    print(avg13_initial)

    # 7hz 자극 후 평균
    c = Fp1_FFT.loc[44:64, '6.50Hz':'7.50Hz']  # 자극 후 범위 다시 지정해야함
    c
    sum7_after = 0
    for i in range(0, 20):
        for j in range(0, 30):
            sum7_after = sum7_after + c.iloc[i, j]
    avg7_after = sum7_after / 600
    print("7의 자극후값")
    print(avg7_after)

    # 13hz 자극 후 평균
    d = Fp1_FFT.loc[46:66, '12.50Hz':'13.50Hz']  # 자극 후 범위 다시 지정해야함
    d
    sum13_after = 0
    for i in range(0, 20):
        for j in range(0, 30):
            sum13_after = sum13_after + d.iloc[i, j]
    avg13_after = sum13_after / 600
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
        f = open('./result.txt', 'w')
        print("7들어옴")
        f.write('7hz입니다.')
        f.close

    elif (avg7_initial > avg13_after and avg13_initial < avg13_after):
        f = open('./resultㄴ.txt', 'w')
        print("13ㄴㄴㄴ들어옴")
        f.write('13hz입니다.')
        f.close

    else:  # 둘 다 오르거나 떨어진 경우
        print("둘다 오르는경우나 떨어진 경우들어옴")
        if (diff7 > diff13):
            print("둘7들어옴")
            f = open('./result.txt', 'w')
            f.write('7hz입니다.')
            f.close
        elif (diff7 < diff13):
            print("둘13들어옴")
            f = open('./result.txt', 'w')
            f.write('13hz입니다.')
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
#현재 경로
# /Users/nadonghyeon/NeuroFocusData/Mave/2022-06-11_오후 3_56/Fp2_FFT.txt
#파이썬 경로 읽기
Fp1_FFT = pd.read_table(file, sep='\t' , encoding='cp949', float_precision='high')

#자극 시작 시점(행)
startPoint = len(Fp1_FFT)

# 노이즈 값 끝 시점(행)
dumpEndPoint = len(Fp1_FFT) + 35

# 초기값 끝 시점(행)
initialTimeEndPoint = dumpEndPoint + 10

# 종료 시점(행)
TotalEndPoint = initialTimeEndPoint + 25

#일정 시간 기다림
threading.Timer(80, cal()).start()
sys.exit(0)






