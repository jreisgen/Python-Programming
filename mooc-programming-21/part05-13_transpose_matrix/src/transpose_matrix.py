from copy import deepcopy
def transpose(matrix: list):
    newlist = []
    newlist = deepcopy(matrix)
    leng = len(matrix)
    for i in range(0, leng):
        for j in range(0, leng):
            value = matrix[i][j]
            newlist[j][i] = value
    for i in range(0, leng):
        for j in range(0, leng):
            mvalue = newlist[i][j]
            matrix[i][j] = mvalue

if __name__ =="__main__":
    mymatrix = ([1,2], [1,2])
    print(transpose(mymatrix))
    print(mymatrix)