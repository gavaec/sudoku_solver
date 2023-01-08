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
sudoku_normal[0][1] = 9
sudoku_normal[0][2] = 3
sudoku_normal[0][5] = 6
sudoku_normal[0][7] = 4
sudoku_normal[1][0] = 7
sudoku_normal[1][6] = 8
sudoku_normal[1][7] = 9
sudoku_normal[2][5] = 7
sudoku_normal[2][8] = 3
sudoku_normal[3][1] = 2
sudoku_normal[3][2] = 8
sudoku_normal[3][5] = 5
sudoku_normal[3][6] = 7
sudoku_normal[4][3] = 7
sudoku_normal[4][5] = 9
sudoku_normal[5][2] = 7
sudoku_normal[5][3] = 2
sudoku_normal[5][6] = 3
sudoku_normal[5][7] = 5
sudoku_normal[6][0] = 8
sudoku_normal[6][3] = 3
sudoku_normal[7][1] = 4
sudoku_normal[7][2] = 6
sudoku_normal[7][8] = 8
sudoku_normal[8][1] = 5
sudoku_normal[8][3] = 6
sudoku_normal[8][6] = 2
sudoku_normal[8][7] = 3

sudoku_normal[5][1] = 6
sudoku_normal[1][1] = 1
sudoku_normal[6][8] = 5

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
repeat_loop = 0
while repeat_loop < 2:
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
    if success_k == 0:
        repeat_loop += 1
for i in sudoku_normal:
    print(i)
