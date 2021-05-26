list = [1, 2, 3, 4, 5, 6]
pop = [0] * len(list)
'''
while len(list) > 0 :
    print("==================")
    print("receive : ",list)
    pop[i] = list.pop(i)
    if len(list) < 1:
        print("end!!")
    else:
        print("pop num is : ", pop[i])
        print("rest list is : ", list)
    i -= 1

sum = pop[0]

for i in range(1,len(pop)):
    sum += pop[i]
    print("sum is : ",sum)

print("final sum is : ",sum)
'''

def recursive(numbers):
    print("==================")
    print("receive : ",numbers)
    n = len(numbers)-1
    pop[n] = numbers.pop(n)
    if len(numbers) < 1 :
        print("end!!")
    else :
        print("pop num is : ", pop[n])
        print("rest list is : ", numbers)
        return recursive(numbers)

recursive(list)

