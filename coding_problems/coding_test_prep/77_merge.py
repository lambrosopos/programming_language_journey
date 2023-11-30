def merge(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    range_dict = {}

    # Sort intervals based on starting index.
    intervals.sort(key=lambda _: _[0])

    for start, end in intervals:
        new_item = True
        for k, v in range_dict.items():
            if k > start:
                continue

            if k <= start <= v:
                new_item = False
                if k <= end <= v:
                    continue
                else:
                    # Increase end range
                    range_dict[k] = end

        if new_item:
            range_dict[start] = end
        
    return list(range_dict.items())

def test_p77_merge():
    intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
    answer = [(1, 3), (4, 10), (20, 25)]
    print(merge(intervals), answer)

    intervals = [(1, 3), (5, 8), (4, 10), (20, 25), (22, 27)]
    answer = [(1, 3), (4, 10), (20, 27)]
    print(merge(intervals), answer)

    intervals = [(19, 21), (1, 3), (3, 8), (4, 10), (20, 25), (22, 24)]
    answer = [(1, 10), (19, 25)]
    print(merge(intervals), answer)

def main():
    test_p77_merge()

main()
