print("\n===== 구구단 출력 프로그램 =======\n")
'''
n = int(input("첫번째 단을 입력하세요 : "))
m = int(input("두번째 단을 입력하세요 : "))
'''
print("출력할 범위의 단을 입력하시오 : ",)
n,m = map(int,input().split())
print("\n------ 결과값 ---------")

if n > m:
    for i in range(0, n-m+1):
        print("\n[ ",m+i,"단 ]")
        for j in range(1, 10):
            result = (m+i) * j
            print((m+i)," x ", j, " = ", result)
elif n <= m:
    for i in range(0, m-n+1):
        print("\n[ ",n+i,"단 ]")
        for j in range(1, 10):
            result = (n+i) * j
            print((n+i)," x ", j, " = ", result)
        print()
else:
    print("\n잘못된 입력입니다.")







