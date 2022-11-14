def is_diagonal(matr):
    total = True
    for i in range(len(matr)):
        for j in range(len(matr)):
            if matr[i][i] == 0:
                total = False
            elif i != j and matr[i][j] != 0:
                total = False
    return total
print(is_diagonal([[1,0,0],[0,1,0],[0,0,1]]))
print(is_diagonal([[1,1,1],[2,4,0],[3,3,3]]))