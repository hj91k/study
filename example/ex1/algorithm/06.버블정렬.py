list = [7, 4, 5, 1, 3]
temp = 0

print("입력된 list ",list,"\n")

for i in range(1,len(list)):
    n = 1
    m = 0
    for j in range(1,len(list)):
        if list[m] > list[n]:
            temp = list[m]
            list[m] = list[n]
            list[n] = temp
        n += 1
        m += 1
    print(i, "회전 결과 ", list)

print("\n최종 정렬된 list ",list)