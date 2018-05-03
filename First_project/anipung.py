from random import randint
import copy


def make_random_matrix():
    # rand_matrix = [[randint(1, 5) for r in range(0, 5)] for e in range(0, 5)]
    rand_matrix = [[1, 1, 1, 2, 2],
                    [3, 2, 4, 2, 3],
                    [1, 2, 4, 3, 3],
                    [1, 4, 4, 4, 2],
                    [1, 2, 2, 3, 2]]

    result_matrix = copy.copy(rand_matrix)
    column_list = []

    for line, line_list in enumerate(rand_matrix):
        print(line_list)

    for i in range(0, 5):
        column_list.append([rand_matrix[j][i] for j in range(0, 5)])

    # 가로 체크
    for line, line_list in enumerate(rand_matrix):
        for i in range(1, 5):
            count = line_list.count(i)
            if count >= 3:
                # 십자가
                start_index = line_list.index(i)
                for k in range(0, 5):
                    if column_list[start_index].count(k) >= 3:
                        # 채우기 전에 블록 내려오기
                        try:
                            y_index = column_list.index(k)
                        except:
                            continue
                        if y_index == 0:
                            # 0 으로 채우기
                            for y in range(y_index, 5):
                                result_matrix[line][y] = 0
                        else:
                            # 0 으로 채우기
                            for y in range(0, y_index):
                                result_matrix[line - y_index] = rand_matrix[0]
                                result_matrix[line][y] = 0
                    else:
                        continue

                # 십자가 아니고 가로만
                if line == 0:
                    for x in range(start_index, 5-count):
                        result_matrix[line][x] = 0
                        pass
                else:
                    for j in range(0, line):
                        for x in range(start_index, 5-count+start_index):
                            result_matrix[line - j][x] = rand_matrix[line - j - 1][x]
                            result_matrix[line][x] = 0
            else:
                continue

    # 세로 체크
    for column, column_list in enumerate(column_list):
        for i in range(0, 5):
            if column_list.count(i) >= 3:
                if column_list.count(i) == 3:
                    pass
                elif column_list.count(i) == 4:
                    pass
                elif column_list.count(i) == 5:
                    pass

    print('---------------')
    for line, line_list in enumerate(result_matrix):
        print(line_list)

make_random_matrix()
