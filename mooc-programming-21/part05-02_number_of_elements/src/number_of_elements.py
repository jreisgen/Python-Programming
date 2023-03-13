def count_matching_elements(my_matrix: list, element1: int):
    counter = 0
    for row in my_matrix:
        for element in row:
            if element == element1:
                counter +=1
    return counter

if __name__ == "__main__":
    matrix1 = [[1,2,3,4], [2,3,4,4], [2,1,3,2]]
    print(count_matching_elements(matrix1, 2))
