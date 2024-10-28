import pandas as pd
import os
import random
import threading
from time import sleep
import sys

# Calculation function
def cal(dumpEndPoint, initialTimeEndPoint, TotalEndPoint):
    # 7hz initial value average
    Fp1_FFT = pd.read_table(file, sep='\t', encoding='cp949', float_precision='high')
    a = Fp1_FFT.loc[dumpEndPoint:initialTimeEndPoint, '6.50Hz':'7.50Hz']

    print("Pandas size count")
    print(a.size)
    print("Pandas row and column count")
    print(a.shape)
    sum7_initial = 0
    print("Row count")
    print(initialTimeEndPoint - dumpEndPoint)
    print("Column count")
    print(TotalEndPoint - (initialTimeEndPoint + 1))
    for i in range(0, initialTimeEndPoint - dumpEndPoint):
        for j in range(0, 30):
            sum7_initial += a.iloc[i, j]
    avg7_initial = sum7_initial / ((initialTimeEndPoint - dumpEndPoint) * 30)
    print("Initial value count")
    print((initialTimeEndPoint - dumpEndPoint) * 30)
    print("7hz initial value")
    print(avg7_initial)

    # 13hz initial value average
    Fp1_FFT = pd.read_table(file, sep='\t', encoding='cp949', float_precision='high')
    b = Fp1_FFT.loc[dumpEndPoint:initialTimeEndPoint, '12.50Hz':'13.50Hz']
    sum13_initial = 0
    for i in range(0, initialTimeEndPoint - dumpEndPoint):
        for j in range(0, 30):
            sum13_initial += b.iloc[i, j]
    avg13_initial = sum13_initial / ((initialTimeEndPoint - dumpEndPoint) * 30)
    print("13hz initial value")
    print(avg13_initial)

    # 7hz post-stimulation average
    Fp1_FFT = pd.read_table(file, sep='\t', encoding='cp949', float_precision='high')
    c = Fp1_FFT.loc[initialTimeEndPoint + 1:TotalEndPoint, '6.50Hz':'7.50Hz']
    sum7_after = 0
    for i in range(0, TotalEndPoint - (initialTimeEndPoint + 1)):
        for j in range(0, 30):
            sum7_after += c.iloc[i, j]
    avg7_after = sum7_after / ((TotalEndPoint - (initialTimeEndPoint + 1)) * 30)
    print("7hz post-stimulation value")
    print(avg7_after)

    # 13hz post-stimulation average
    Fp1_FFT = pd.read_table(file, sep='\t', encoding='cp949', float_precision='high')
    d = Fp1_FFT.loc[initialTimeEndPoint + 1:TotalEndPoint, '12.50Hz':'13.50Hz']
    sum13_after = 0
    for i in range(0, TotalEndPoint - (initialTimeEndPoint + 1)):
        for j in range(0, 30):
            sum13_after += d.iloc[i, j]
    avg13_after = sum13_after / ((TotalEndPoint - (initialTimeEndPoint + 1)) * 30)
    print("13hz post-stimulation value")
    print(avg13_after)

    # Calculate difference
    diff7 = avg7_after - avg7_initial
    diff13 = avg13_after - avg13_initial
    print("7hz difference")
    print(diff7)
    print("13hz difference")
    print(diff13)

    # Choose a filename (add random number)
    randomnum = random.randint(0, 10000)
    filename = 'result' + str(randomnum) + '.txt'
    
    # Process result based on difference
    # Display result (open text file)
    if (avg7_initial < avg13_after and avg13_initial > avg13_after):
        with open('../Web/Pages/' + filename, 'w') as f:
            print("7 entered")
            f.write('7hz')

    elif (avg7_initial > avg13_after and avg13_initial < avg13_after):
        with open('../Web/Pages/' + filename, 'w') as f:
            print("13 entered")
            f.write('13hz')

    else:  # Both increase or decrease
        print("Both increase or decrease entered")
        if (diff7 > diff13):
            print("Both 7 entered")
            with open('../Web/Pages/' + filename, 'w') as f:
                f.write('7hz')
        elif (diff7 < diff13):
            print("Both 13 entered")
            with open('../Web/Pages/' + filename, 'w') as f:
                f.write('13hz')


# Start Python main file

# The Python file opens when the brainwave analysis button is clicked on the web, but add 80 seconds to the measurement time (1 min 10 sec) for data to arrive before starting

# Open file by accessing path
path = 'C:/MAVE_RawData/'

file_list = os.listdir(path)
# Count files in folder
number_files = len(file_list)
print(number_files)
set_index = number_files - 1

real_path = path + file_list[set_index] + "/"
print(real_path)

file_list2 = os.listdir(path + file_list[set_index])
print(file_list2[1])

file = real_path + file_list2[1]
print(file)

# Current path (Mac)
# /Users/nadonghyeon/NeuroFocusData/Mave/2022-06-11_오후 3_56/Fp2_FFT.txt
# Windows
# C:/MAVE_RawData/2022-06-11_오후 3_56/Fp1_FFT.txt

# Create table
Fp1_FFT = pd.read_table(file, sep='\t', encoding='cp949', float_precision='high')

# Actual stimulation start point (row)
startPoint = len(Fp1_FFT) - 2
# startPoint = 0

print("Start point")
print(startPoint)

# Noise end point (row) (initial value calculation measurement point)
dumpEndPoint = startPoint + 35
print("Initial value calculation measurement")
print(dumpEndPoint)

# Initial value end point (row) (initial value calculation end point) (stimulation calculation measurement point)
initialTimeEndPoint = dumpEndPoint + 10
print("Stimulation calculation point")
print(initialTimeEndPoint)

# End point (row) (stimulation end point)
TotalEndPoint = initialTimeEndPoint + 25
print("Stimulation end")
print(TotalEndPoint)

# Wait for calculation
sleep(75)

# Wait for a set time (loading time)
cal(dumpEndPoint, initialTimeEndPoint, TotalEndPoint)
