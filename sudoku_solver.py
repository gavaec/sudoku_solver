def possible_for_number(k_, i_def, j_def):
    i_sqr_ = i_def // 3 * 3 + j_def // 3
    if k_ in sudoku_transpose[j_def]:
        return False
    elif k_ in sudoku_square[i_sqr_]:
        return False
    elif k_ in sudoku_normal[i_def]:
        return False
    else:
        return True


sudoku_normal = []
for i in range(0, 9):
    sudoku_normal.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
sudoku_normal[0][5] = 5
sudoku_normal[0][7] = 9
sudoku_normal[1][2] = 9
sudoku_normal[1][3] = 2
sudoku_normal[1][4] = 3
sudoku_normal[1][7] = 7
sudoku_normal[2][1] = 8
sudoku_normal[2][2] = 2
sudoku_normal[2][3] = 9
sudoku_normal[2][6] = 1
sudoku_normal[3][1] = 9
sudoku_normal[3][2] = 1
sudoku_normal[3][7] = 8
sudoku_normal[3][8] = 6
sudoku_normal[5][0] = 8
sudoku_normal[5][1] = 7
sudoku_normal[5][6] = 9
sudoku_normal[5][7] = 3
sudoku_normal[6][2] = 5
sudoku_normal[6][5] = 6
sudoku_normal[6][6] = 7
sudoku_normal[6][7] = 1
sudoku_normal[7][1] = 6
sudoku_normal[7][4] = 7
sudoku_normal[7][5] = 9
sudoku_normal[7][6] = 8
sudoku_normal[8][1] = 1
sudoku_normal[8][3] = 5

for i in sudoku_normal:
    print(i)
print(' ')

sudoku_transpose = []
for j in range(0, 9):
    tmp = []
    for i in range(0, 9):
        tmp.append(sudoku_normal[i][j])
    sudoku_transpose.append(tmp)

sudoku_square = []
for i in range(0, 3):
    for j in range(0, 3):
        tmp = []
        for i_ in range(i*3, i*3 + 3):
            for j_ in range(j * 3, j * 3 + 3):
                tmp.append(sudoku_normal[i_][j_])
        sudoku_square.append(tmp)
success_k = 1
while success_k > 0:
    success_k = 0
    for k in range(1, 10):
        for i in range(0, 9):
            if k not in sudoku_normal[i]:
                count_k = 0
                j = -1
                while count_k < 2 and j < 8:
                    j += 1
                    if sudoku_normal[i][j] == 0:
                        if possible_for_number(k, i, j):
                            count_k += 1
                            j_possible = j
                if count_k == 1:
                    i_sqr = i // 3 * 3 + j_possible // 3
                    sudoku_normal[i][j_possible] = k
                    sudoku_transpose[j_possible][i] = k
                    sudoku_square[i_sqr].append(k)
                    success_k += 1
        for i in range(0, 3):
            for j in range(0, 3):
                count_k = 0
                i_sqr = i * 3 + j
                if k not in sudoku_square[i_sqr]:
                    for i_ in range(i * 3, i * 3 + 3):
                        for j_ in range(j * 3, j * 3 + 3):
                            if sudoku_normal[i_][j_] == 0:
                                if possible_for_number(k, i_, j_):
                                    count_k += 1
                                    i_possible = i_
                                    j_possible = j_
                if count_k == 1:
                    sudoku_normal[i_possible][j_possible] = k
                    sudoku_transpose[j_possible][i_possible] = k
                    sudoku_square[i_sqr].append(k)
                    success_k += 1
    print(success_k)
for i in sudoku_normal:
    print(i)
