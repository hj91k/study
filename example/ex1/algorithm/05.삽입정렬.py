list = [8, 5, 6, 2, 4]
temp = 0
print("입력된 list ",list,"\n")

for i in range(1,len(list)):
    n = i
    for j in range(1,i+1):
        if list[i-j] > list[n]:
            temp = list[i-j]
            list[i-j] = list[n]
            list[n] = temp
            n -= 1
        print(i,"회전 결과 ",list)

print("\n최종 정렬된 list ",list)