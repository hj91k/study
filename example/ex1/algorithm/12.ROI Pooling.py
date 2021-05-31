import random
import numpy as np

total_Array = np.array([[0] * 256 for i in range(128)])

for y in range(0,128):
    for x in range(0,256):
        total_Array[y][x] = random.randint(0,255)

t = 0
X = np.array([float(0)] * 2)
Y = np.array([float(0)] * 2)

while t == 0 :
    X[0] = random.uniform(0,127)
    X[1] = random.uniform(0,127)
    Y[0] = random.uniform(0,255)
    Y[1] = random.uniform(0,255)
    if X[0] + float(10) <= X[1] and Y[0] + float(10) <= Y[1]:
        t = 1

print(X,Y)

def rounding(number) :
    if number % 1 >= 0.5:
        return int(number)+1
    else :
        return int(number)

X[0] = rounding(X[0])
X[1] = rounding(X[1])
Y[0] = rounding(Y[0])
Y[1] = rounding(Y[1])

print(X,Y)

def calcCropindex(start, end, divide):
    a = int(int(end-start) / divide)
    b = int(end-start) % divide

    index = [0] * (divide+1)

    for i in range(divide+1):
        if i == 0:
            index[i] = int(start)
        elif i <= b:
            index[i] = int(index[i-1] + a +1)
        else :
            index[i] = int(index[i-1] + a)
    return index

x_index = calcCropindex(X[0],X[1],3)
y_index = calcCropindex(Y[0],Y[1],3)

print("인덱스 값 :",x_index,y_index)

def maxpooling(X_Start,X_End,Y_Start,Y_End,Array):
    max = 0
    for i in range(X_Start,X_End):
        for j in range(Y_Start,Y_End):
            if int(Array[X_Start][Y_Start]) > max:
                max = int(Array[X_Start][Y_Start])
    return max

Result_Array = [[0]*3 for i in range(3)]

for i in range(3):
    for j in range(3):
        Result_Array[i][j] = maxpooling(x_index[i],x_index[i+1], y_index[j],y_index[j+1], total_Array)

print("Maxpooling 결과 :",Result_Array)
