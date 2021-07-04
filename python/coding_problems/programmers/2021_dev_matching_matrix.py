import time
from pprint import pprint

def solution(rows, columns, queries):
    # rows = 3, columns = 2
    # range(1, 6 + 2, 3) => 1, 4, 7
    # list(range(1, 1 % rows * columns + 1))
    matrix = [list(range(_, _ + columns)) for _ in range(1, rows * columns + 1, rows)]
    
   	# query => 4 번째보다 현 y2 가 적으면 아래로 하강~
   	# query => 3 번째보다 현 x2 가 적으면 왼쪽으로~
   	# query => 2 번째보다 현 x1 가 적으면 위로~

    answer = []
    
    for query in queries:
        start_query = [query[0] - 1, query[1] - 1]
        current_position = start_query
        curr_num = temp_num = matrix[start_query[0]][start_query[1]]

        direction = 'RIGHT'
        right_boundary = query[3] - 1
        down_boundary = query[2] - 1
        left_boundary = query[1] - 1
        up_boundary = query[0] - 1

        def get_num(position):
            return matrix[position[0]][position[1]]

        def set_num(curr_pos, num):
            matrix[curr_pos[0]][curr_pos[1]] = num

        def make_change(current_position, curr_num, temp_num):
            # print(f"{temp_num=}, {curr_num=}")
            temp_num = get_num(current_position)
            set_num(current_position, curr_num)
            curr_num = temp_num
            return curr_num, temp_num

        min_num = curr_num

        flag = True
        while flag:
            if direction == "RIGHT":
                if (current_position[1] + 1) <= right_boundary:
                    current_position[1] += 1
                    curr_num, temp_num = make_change(current_position, curr_num, temp_num)
                else:
                    direction = "DOWN"
            elif direction == "DOWN":
                if (current_position[0] + 1) <= down_boundary:
                    current_position[0] += 1
                    curr_num, temp_num = make_change(current_position, curr_num, temp_num)
                else:
                    direction = "LEFT"
            elif direction == "LEFT":
                if (current_position[1] - 1) >= left_boundary:
                    current_position[1] -= 1
                    curr_num, temp_num = make_change(current_position, curr_num, temp_num)
                else:
                    direction = "UP"
            elif direction == "UP":
                if (current_position[0] -1) >= up_boundary:
                    current_position[0] -= 1
                    curr_num, temp_num = make_change(current_position, curr_num, temp_num)
                else:
                    answer.append(min_num)
                    flag = False
            min_num = min(min_num, curr_num)
            # print(f"Current direction: {direction}")
            # print(f"Current position: {current_position}")
            # time.sleep(1)
            # pprint(matrix)
    return answer

if __name__ == "__main__":
    rows = 100
    columns = 97
    queries = [[1,1,100,97]]

    pprint(solution(rows, columns, queries))
