total = 3500
x = 500
y = 700
z = 400

print("\n현재 당신이 소유하고 있는 금액 :",total)

for i in range(1,int(total/x)):
    for j in range(1,int(total/y)):
        for k in range(1,int(total/z)):
            if total == (x * i + y * j + z * k):
                print("크림빵",i,"개, 새우깡",j,"개, 콜 라",k,"개")

print("어떻게 구입하시겠습니까?")