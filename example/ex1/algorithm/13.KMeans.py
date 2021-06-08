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
    plt.scatter(c0, 0, s=200, c="r")
    plt.scatter(c1, 0, s=200, c="b")
    plt.scatter(c2, 0, s=200, c="g")
    plt.show()


X = np.array([[2, 0], [3, 0], [4, 0], [10, 0], [11, 0], [12, 0],
              [20, 0], [25, 0], [30, 0]])
Y = np.array([0,0,0,0,0,0,0,0,0])
plt.scatter(X[:, 0], X[:, 1], s=100)
plt.show()

t = 0
while t == 0:
    c0 = random.randint(1, 30)
    c1 = random.randint(1, 30)
    c2 = random.randint(1, 30)
    if c0 != c1 and c0 != c2 and c1 != c2:
        t = 1

plot_cluster(Y,c0,c1,c2)

total_count = 0
sum_c0 = sum_c1 = sum_c2 = 0
count_c0 = count_c1 = count_c2 = 0

def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

for i in range(len(X)):
    distance_c0 = euclidean_distance(c0,X[i][0])
    distance_c1 = euclidean_distance(c1,X[i][0])
    distance_c2 = euclidean_distance(c2,X[i][0])
    if distance_c0 == min(distance_c0,distance_c1,distance_c2):
        Y[i] = 0
        sum_c0 += X[i][0]
        count_c0 += 1
    elif distance_c1 == min(distance_c0,distance_c1,distance_c2):
        Y[i] = 1
        sum_c1 += X[i][0]
        count_c1 += 1
    elif distance_c2 == min(distance_c0,distance_c1,distance_c2):
        Y[i] = 2
        sum_c2 += X[i][0]
        count_c2 += 1

plot_cluster(Y,c0,c1,c2)

c0 = int(sum_c0 / count_c0)
c1 = int(sum_c1 / count_c1)
c2 = int(sum_c2 / count_c2)

while total_count < 100 :
    sum_c0 = sum_c1 = sum_c2 = 0
    count_c0 = count_c1 = count_c2 = 0

    for i in range(len(X)):
        distance_c0 = euclidean_distance(c0, X[i][0])
        distance_c1 = euclidean_distance(c1, X[i][0])
        distance_c2 = euclidean_distance(c2, X[i][0])
        if distance_c0 == min(distance_c0, distance_c1, distance_c2):
            Y[i] = 0
            sum_c0 += X[i][0]
            count_c0 += 1
        elif distance_c1 == min(distance_c0, distance_c1, distance_c2):
            Y[i] = 1
            sum_c1 += X[i][0]
            count_c1 += 1
        elif distance_c2 == min(distance_c0, distance_c1, distance_c2):
            Y[i] = 2
            sum_c2 += X[i][0]
            count_c2 += 1

    if c0 == int(sum_c0/count_c0) and c1 == int(sum_c1/count_c1) and c2 == int(sum_c2/count_c2) :
        total_count += 1
    else :
        total_count = 0
        c0 = int(sum_c0 / count_c0)
        c1 = int(sum_c1 / count_c1)
        c2 = int(sum_c2 / count_c2)
        plot_cluster(Y, c0, c1, c2)

plot_cluster(Y, c0, c1, c2)