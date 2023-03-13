def block_correct(sudoku: list, row_no: int, column_no: int):
    bool = True
    i = row_no
    j = column_no
    newMatrix = []
    newlist = []
    newMatrix.append(sudoku[i][j])
    newMatrix.append(sudoku[i+1][j])
    newMatrix.append(sudoku[i][j+1])
    newMatrix.append(sudoku[i+1][j+1])
    newMatrix.append(sudoku[i+2][j+1])
    newMatrix.append(sudoku[i+1][j+2])
    newMatrix.append(sudoku[i+2][j+2])
    newMatrix.append(sudoku[i+2][j])
    newMatrix.append(sudoku[i][j+2])
    
    a = 0
    while a < len(newMatrix):
        value = newMatrix[a]
        if value in newlist and value !=0:
            bool = False
            break
        else:
            newlist.append(value)
            a +=1
    return bool

if __name__ == "__main__":

    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    
    print(block_correct(sudoku, 3, 3))