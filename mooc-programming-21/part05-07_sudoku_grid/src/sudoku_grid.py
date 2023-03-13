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
    for row in sudoku:
        for element in sudoku:
            if element ==0:
                print("_ ")
            else:
                print(element +" ")
        print()

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

    print(sudoku_grid_correct(sudoku))