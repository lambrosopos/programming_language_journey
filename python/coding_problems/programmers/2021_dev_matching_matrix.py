def solution(rows, columns, queries):
    # rows = 3, columns = 2
    # range(1, 6 + 2, 3) => 1, 4, 7
    # list(range(1, 1 % rows * columns + 1))
    matrix = [list(range(_, _ + columns)) for _ in range(1, rows * columns + 1, rows)]
    
   	# query => 4 번째보다 현 y2 가 적으면 아래로 하강~
   	# query => 3 번째보다 현 x2 가 적으면 왼쪽으로~
   	# query => 2 번째보다 현 x1 가 적으면 위로~
    
    for query in queries:
        start_query, end_query = query[:2], query[3:]
        start_num = matrix[start_query[0]][start_query[1]]
    
    
    
    answer = []
    return answer
