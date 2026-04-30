matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]
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


print(transponirovane(matrix))
print(print_mactrix(matrix))
