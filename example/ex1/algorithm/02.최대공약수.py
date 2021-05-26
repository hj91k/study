print("\n===== 최대공약수 출력 프로그램 =======\n")

##print("두 수를 입력하시오 : ")
##n,m = map(int,input().split())
a = int(input("첫 번째 수를 입력하세요 : "))
b = int(input("두 번째 수를 입력하세요 : "))

GCD = 0
num = 1

if a>b:
    min = b
else:
    min = a

while min >= num:
    if int(a%num) == 0 and int(b%num) == 0:
        GCD = num
    num += 1

print("\n두 수의 최대공약수는",GCD,"입니다.")
