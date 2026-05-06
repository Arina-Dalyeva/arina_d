matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16],
          [17,18,19,20]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 3 == 0:
            print(matrix[i][j])
def print_mactrix (matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = ' ')
        print()


print(print_mactrix(matrix))


def transponirovane (matrix):#20+25+22+16=83-1=82
    for i in range(len(matrix)//2):
        for j in range(i+1, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def perevorashivanie (matrix):
    for i in range(len(matrix)//2):
        for j in range(len(matrix[i])):
            if i == 0:
                matrix[0][j], matrix[-1][j] = matrix[-1][j], matrix[0][j]
                print(matrix)
            else:
                matrix[i][j], matrix[-(i+1)][j] = matrix[-(i+1)][j], matrix[i][j]
                print(matrix)
    return matrix


def transponirovanie_vertikalnoe (matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])//2):
            if j == 0:
                matrix[i][0], matrix[i][-1] = matrix[i][-1], matrix[i][0]
                print(matrix)
            else:
                matrix[i][j], matrix[i][-(j+1)] = matrix[i][-(j+1)], matrix[i][j]
                print(matrix)
    return matrix


print(transponirovanie_vertikalnoe(matrix))
print(print_mactrix(matrix))



