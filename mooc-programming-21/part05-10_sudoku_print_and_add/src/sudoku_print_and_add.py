
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for i in range(row_no, row_no+3):
        for j in range(column_no, column_no+3):
            ting = sudoku[i][j]
            if ting in numbers and ting!=0:
                return False
            else:
                numbers.append(ting)
    return True

def column_correct(sudoku: list, col_no: int):


    i = 0
    newlist = []
    while i < len(sudoku):
        value = sudoku[i][col_no]
        if value in newlist and value != 0:
            return False
        else:
            newlist.append(sudoku[i][col_no])
            i +=1
    return True

def row_correct(sudoku: list, row_no: int):
    i = 0
    newlist = []
    while i < len(sudoku[0]):
        value1 = sudoku[row_no][i]
        if value1 in newlist and value1 != 0:
            return False
        else:
            newlist.append(value1)
            i +=1
    return True

def sudoku_grid_correct(sudoku: list):
    
    h = 0
    i = 0
    for h in range(0, 8, 3):
        for i in range(0, 8, 3):
            value = block_correct(sudoku, h, i)
            if value == False:
                print("Block")
                return False
    

    j = 0
    k = 0
    while j < 9:
        if row_correct(sudoku, j) == False:
            print("row")
            return False
        else:
            j+=1
    while k < 9:
        if column_correct(sudoku, k) == False:
            print("col")
            return False
        else:
            k+=1
    return True
 
def print_sudoku(sudoku: list):
    for i in range(0, 9):
        for j in range(0, 9):
            newValue = sudoku[i][j]
            if newValue == 0:
                sudoku[i][j] = "_"

    print(f"{sudoku[0][0]} {sudoku[0][1]} {sudoku[0][2]}  {sudoku[0][3]} {sudoku[0][4]} {sudoku[0][5]}  {sudoku[0][6]} {sudoku[0][7]} {sudoku[0][8]}")
    print(f"{sudoku[1][0]} {sudoku[1][1]} {sudoku[1][2]}  {sudoku[1][3]} {sudoku[1][4]} {sudoku[1][5]}  {sudoku[1][6]} {sudoku[1][7]} {sudoku[1][8]}")
    print(f"{sudoku[2][0]} {sudoku[2][1]} {sudoku[2][2]}  {sudoku[2][3]} {sudoku[2][4]} {sudoku[2][5]}  {sudoku[2][6]} {sudoku[2][7]} {sudoku[2][8]}")
    print()
    print(f"{sudoku[3][0]} {sudoku[3][1]} {sudoku[3][2]}  {sudoku[3][3]} {sudoku[3][4]} {sudoku[3][5]}  {sudoku[3][6]} {sudoku[3][7]} {sudoku[3][8]}")
    print(f"{sudoku[4][0]} {sudoku[4][1]} {sudoku[4][2]}  {sudoku[4][3]} {sudoku[4][4]} {sudoku[4][5]}  {sudoku[4][6]} {sudoku[4][7]} {sudoku[4][8]}")
    print(f"{sudoku[5][0]} {sudoku[5][1]} {sudoku[5][2]}  {sudoku[5][3]} {sudoku[5][4]} {sudoku[5][5]}  {sudoku[5][6]} {sudoku[5][7]} {sudoku[5][8]}")
    print()
    print(f"{sudoku[6][0]} {sudoku[6][1]} {sudoku[6][2]}  {sudoku[6][3]} {sudoku[6][4]} {sudoku[6][5]}  {sudoku[6][6]} {sudoku[6][7]} {sudoku[6][8]}")
    print(f"{sudoku[7][0]} {sudoku[7][1]} {sudoku[7][2]}  {sudoku[7][3]} {sudoku[7][4]} {sudoku[7][5]}  {sudoku[7][6]} {sudoku[7][7]} {sudoku[7][8]}")
    print(f"{sudoku[8][0]} {sudoku[8][1]} {sudoku[8][2]}  {sudoku[8][3]} {sudoku[8][4]} {sudoku[8][5]}  {sudoku[8][6]} {sudoku[8][7]} {sudoku[8][8]}")

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number


    
if __name__ == "__main__":
    sudoku = [
    [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [ 0, 5, 1, 6, 0, 0, 8, 3, 9 ],
    [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ]]


    print_sudoku(sudoku)