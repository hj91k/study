import numpy as np
import matplotlib.pyplot as plt
import random

def plot_cluster(labels, c0, c1, c2):
    plt.scatter(X[labels == 0, 0],
                X[labels == 0, 1], s=100, marker='v', c='r')
    plt.scatter(X[labels == 1, 0],
                X[labels == 1, 1], s=100, marker='^', c='b')
    plt.scatter(X[labels == 2, 0],
                X[labels == 2, 1], s=100, marker='v', c='g')
    plt.scatter(c0[0], c0[1], s=200, c="r")
    plt.scatter(c1[0], c1[1], s=200, c="b")
    plt.scatter(c2[0], c2[1], s=200, c="g")
    plt.show()

X = np.array([[2, 1], [3, 5], [4, 10], [10, 30], [11, 20], [12, 25],
              [20, 18], [25, 21], [30, 24]])
Y = np.array([0,0,0,0,0,0,0,0,0])
plt.scatter(X[:, 0], X[:, 1], s=100)
plt.show()

def euclidean_distance(x, y):
    number = np.sqrt(((x[0] - y[0]) ** 2) + (x[1] - y[1]) ** 2)
    if number % 1 >= 0.5:
        return int(number) + 1
    else:
        return int(number)

def Center_Reset(sum, count):
    result = np.array([0] * 2)
    if count != 0 :
        result[0] = int(sum[0] / count)
        result[1] = int(sum[1] / count)
        return result

def same_discriminator(x,y):
    if x[0] == y[0] and x[1] == y[1]:
        return True
    else :
        return False

t = 0
while t == 0:
    c0 = np.array([random.randint(1, 30),random.randint(1, 30)])
    c1 = np.array([random.randint(1, 30),random.randint(1, 30)])
    c2 = np.array([random.randint(1, 30),random.randint(1, 30)])
    if same_discriminator(c0,c1) != True and same_discriminator(c0,c2) != True and same_discriminator(c1,c2) != True :
        t = 1

plot_cluster(Y,c0,c1,c2)

total_count = 0
sum_c0 = np.array([0]*2)
sum_c1 = np.array([0]*2)
sum_c2 = np.array([0]*2)
count_c0 = count_c1 = count_c2 = 0

for i in range(len(X)):
    distance_c0 = euclidean_distance(c0,X[i])
    distance_c1 = euclidean_distance(c1,X[i])
    distance_c2 = euclidean_distance(c2,X[i])

    if distance_c0 == min(distance_c0,distance_c1,distance_c2):
        Y[i] = 0
        sum_c0[0] += X[i][0]
        sum_c0[1] += X[i][1]
        count_c0 += 1
    elif distance_c1 == min(distance_c0,distance_c1,distance_c2):
        Y[i] = 1
        sum_c1[0] += X[i][0]
        sum_c1[1] += X[i][1]
        count_c1 += 1
    elif distance_c2 == min(distance_c0,distance_c1,distance_c2):
        Y[i] = 2
        sum_c2[0] += X[i][0]
        sum_c2[1] += X[i][1]
        count_c2 += 1

plot_cluster(Y,c0,c1,c2)


c0 = Center_Reset(sum_c0,count_c0)
c1 = Center_Reset(sum_c1,count_c1)
c2 = Center_Reset(sum_c2,count_c2)

plot_cluster(Y,c0,c1,c2)

New_c0 = np.array([0]*2)
New_c1 = np.array([0]*2)
New_c2 = np.array([0]*2)

while total_count < 100 :
    sum_c0[0] = sum_c0[1] = 0
    sum_c1[0] = sum_c1[1] = 0
    sum_c2[0] = sum_c2[1] = 0
    count_c0 = count_c1 = count_c2 = 0

    for i in range(len(X)):
        distance_c0 = euclidean_distance(c0, X[i])
        distance_c1 = euclidean_distance(c1, X[i])
        distance_c2 = euclidean_distance(c2, X[i])

        if distance_c0 == min(distance_c0, distance_c1, distance_c2):
            Y[i] = 0
            sum_c0[0] += X[i][0]
            sum_c0[1] += X[i][1]
            count_c0 += 1

        elif distance_c1 == min(distance_c0, distance_c1, distance_c2):
            Y[i] = 1
            sum_c1[0] += X[i][0]
            sum_c1[1] += X[i][1]
            count_c1 += 1

        elif distance_c2 == min(distance_c0, distance_c1, distance_c2):
            Y[i] = 2
            sum_c2[0] += X[i][0]
            sum_c2[1] += X[i][1]
            count_c2 += 1

    New_c0 = Center_Reset(sum_c0, count_c0)
    New_c1 = Center_Reset(sum_c1, count_c1)
    New_c2 = Center_Reset(sum_c2, count_c2)

    if same_discriminator(c0,New_c0) == True and same_discriminator(c1,New_c1) == True and same_discriminator(c2,New_c2) == True :
        total_count += 1
    else:
        total_count = 0
        c0 = Center_Reset(sum_c0, count_c0)
        c1 = Center_Reset(sum_c1, count_c1)
        c2 = Center_Reset(sum_c2, count_c2)
        plot_cluster(Y, c0, c1, c2)

plot_cluster(Y, c0, c1, c2)

