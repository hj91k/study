ax = int(input("첫 번째 행의 크기를 입력하시오 : "))
ay = int(input("첫 번째 열의 크기를 입력하시오 : "))
print()

a = [[0] * ay for i in range(ax)]

for i in range(0,ax):
    for j in range(0,ay):
        print("[",i+1,"][",j+1,"]의 값을 입력하세요 : ",)
        a[i][j] =int(input())

print()
bx = int(input("두 번째 행의 크기를 입력하시오 : "))
by = int(input("두 번째 열의 크기를 입력하시오 : "))

b = [[0] * by for i in range(bx)]

for i in range(0,bx):
    for j in range(0,by):
        print("[",i+1,"][",j+1,"]의 값을 입력하세요 : ",)
        b[i][j] =int(input())

result = [[0] * by for i in range(ax)]

if ay == bx:
    for A in range(0,ax):
        for B in range(0,by):
            for C in range(0,ay):
                result[A][B] += int(a[A][C] * b[C][B])
    print(a,"x",b,"=",result)

else:
    print("행렬 곱을 할 수 없습니다.")
