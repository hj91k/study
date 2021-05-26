list = [9, 6, 7, 3, 5]
temp = 0
min = 0

print("입력된 list ",list,"\n")

for i in range(0,len(list)-1):
    count = i
    while count<len(list)-1:
        if list[count] < list[count+1]:
            min = count
        elif list[count] > list[count+1]:
            min = count+1
        count += 1
    if list[i] > list[min]:
        temp = list[i]
        list[i] = list[min]
        list[min] = temp

    print(i+1, "회전 결과 ", list)

print("\n최종 정렬된 list ",list)
