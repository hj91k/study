class CNN:
    def __init__(self,input,filter,stride):
        self.input = input
        self.filter = filter
        self.stride = stride

    def convolution(self):
        Outputsize = int((len(self.input) - len(self.filter)) / self.stride + 1)
        Output = [[0] * Outputsize for i in range(Outputsize)]
        for i in range(Outputsize):
            for j in range(Outputsize):
                sum = 0
                for n in range(len(self.filter)):
                    for m in range(len(self.filter)):
                        sum += self.input[n + i * self.stride][m + j * self.stride] * self.filter[n][m]
                Output[i][j] = sum
        return Output

    def maxpooling(self,input,window):
        Outputsize = int(len(input)/window)
        Output = [[0] * Outputsize for i in range(Outputsize)]

        for i in range(Outputsize):
            for j in range(Outputsize):
                max = 0
                for n in range(window):
                    for m in range(window):
                        if max < input[n + i * window][m + j * window]:
                            max = input[n + i * window][m + j * window]
                Output[i][j] = max
        return Output


input = [1, 2, 3, 0], [0, 1, 2, 3], [3, 0, 1, 2],[2, 4, 0, 1]
filter = [2, 0, 1], [0, 1, 2], [1, 0, 2]
stride = 1

c1 = CNN(input,filter,stride)
convol_output = c1.convolution()
maxpool_output = c1.maxpooling(c1.input,2)

print("convolution 결과 :",convol_output,", maxpool 결과 :",maxpool_output)

'''        
def convolution(Input,Filter,Stride):
    Outputsize = int((len(Input)-len(Filter))/Stride +1)
    Output = [[0] * Outputsize for i in range(Outputsize)]
    for i in range(Outputsize):
        for j in range(Outputsize):
            sum = 0
            for n in range(len(Filter)):
                for m in range(len(Filter)):
                    sum += Input[n + i * Stride][m + j * Stride] * Filter[n][m]
            Output[i][j] = sum
    return Output
'''

