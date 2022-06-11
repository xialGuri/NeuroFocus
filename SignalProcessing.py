import pandas as pd
import os
import xlsxwriter
import numpy as np
from datetime import datetime, timedelta
# 파일 경로로 접근해서 파일 열기
path = '/Users/nadonghyeon/NeuroFocusData/Mave/'

file_list = os.listdir(path)
print(file_list)

real_path = path +file_list[2] + "/"

file_list2 = os.listdir(path + file_list[2])
print(file_list2[1])

file  = real_path + file_list2[1]
print(file)

Fp1_FFT = pd.read_csv(file, delimiter='\t', encoding='cp949')
# /Users/nadonghyeon/NeuroFocusData/Mave/2022-06-11_오후 3_56/Fp2_FFT.txt
