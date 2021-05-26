list = [7, 5, 9, 8, 2]

def devide(numbers):
    if int(len(numbers) % 2) == 1:
        n = int(len(numbers)/2)+1
    else :
        n = int(len(numbers)/2)
    member_left = numbers[:n]
    member_right = numbers[n:]

    if len(member_left) > 2:
        devide(member_left)
    elif len(member_right) > 2:
        devide(member_right)
    return member_left,member_right

def combine(A,B):
    temp = 0
    for x in range(len(A)-1):
        for y in range(1,len(A)-1):
            n = x+y
            if A[x] > A[n] :
                temp = A[x]
                A[x] = A[n]
                A[n] = temp

    for x in range(len(B)-1):
        for y in range(1,len(B)):
            n = x+y
            if B[x] > B[n] :
                temp = B[x]
                B[x] = B[n]
                B[n] = temp

    print(A,B)
    X = A + B
    print(X)

    for i in range(len(B)):
        m = len(A)+i
        for j in range(len(A)+1):
            if X[m] < X[j]:
                X.insert(j,X[m])
                del(X[m+1])
    return X

a,b = devide(list)
A = combine(a,b)

print(A)

