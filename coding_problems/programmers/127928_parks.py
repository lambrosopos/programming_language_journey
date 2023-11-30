def solution(park, routes):
    H, W = len(park), len(park[0])
    start_pos = None
    for i in range(H):
        for j in range(W):
            if park[i][j] == "S":
                start_pos = [i, j]

    cur_pos = start_pos
    for r in routes:
        direction, squares = r.split()
        if direction == "E":
            next_pos = [cur_pos[0], cur_pos[1] + squares]
        elif direction == "W":
            next_pos = [cur_pos[0], cur_pos[1] - squares]
        elif direction == "S":
            next_pos = [cur_pos[0] + squares, cur_pos[1]]
        elif direction == "N":
    	    next_pos = [cur_pos[0] - squares, cur_pos[1]]
    	# Check if out of bounds
        if next_pos[0] < 0 or next_pos[0] >= H or next_pos[1] < 0 or next_pos[1] >= W:
    	    continue
		# Check if obstacles between
        is_clear = True
        for i in range(cur_pos[0], next_pos[0]):
            for j in range(cur_pos[1], next_pos[1]):
                if park[i][j] == "X":
                    is_clear = False
                    break
        if is_clear:
            cur_pos = next_pos
    return cur_pos
