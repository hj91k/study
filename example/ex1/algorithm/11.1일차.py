
'''
def shortest_line(list):
    Min = list[4] - list[0]
    for n in range(3):
        if list[n+2] - list[n] < Min:
            Min = list[n+2] -list[n]
    return Min

spots = [1,3,7,20,26]

print("입력된 점 :", spots)
print("최소 선분 길이 :", shortest_line(spots))

temp = 0
for i in range(len(spots)):
    for j in range(len(spots)):
        if spots[i] < spots[j]:
            temp = spots[i]
            spots[i] = spots[j]
            spots[j] = temp
'''

def shortest_distance(list):
    route_f = 0
    route_m = 3
    route_e = 4
    min = ((list[route_f][0] - list[route_m][0]) ** (2) + (list[route_f][1] - list[route_m][1]) ** (2)) ** (1 / 2) + (
                (list[route_m][0] - list[route_e][0]) ** (2) + (list[route_m][1] - list[route_e][1]) ** (2)) ** (1 / 2)
    for i in range(4):
        for j in range(i, 5):
            if i != j:
                distance_1 = ((list[i][0] - list[j][0]) ** (2) + (list[i][1] - list[j][1]) ** (2)) ** (1 / 2)
                next = j
                for k in range(5):
                    if k != next and k != i:
                        distance_2 = ((list[next][0] - list[k][0]) ** (2) + (list[next][1] - list[k][1]) ** (
                            2)) ** (1 / 2)
                        total_distance = distance_1 + distance_2
                        if min > total_distance:
                            min = total_distance
                            route_f = i
                            route_m = next
                            route_e = k

    print("최단 경로 :",route_f+1,"-",route_m+1,"-",route_e+1)
    print("최단 거리 :",min)

spots = [1,2],[10,4],[5,3],[6,6],[10,5]

print("입력된 점 위치 :",spots)
shortest_distance(spots)

# num = 1
# print(i+1,"번째 점과",j+1,"번째 점의 거리",distance_1)
# print(next + 1, "번째 점과", k + 1, "번째 점의 거리", distance_2)
# print(num,"번째 결과값 :",total_distance)
# num += 1