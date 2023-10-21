def hIndex(citations: list[int]) -> int:
    citations.sort(reverse=True)
    print(citations)

    total_len = len(citations)
    for idx, val in enumerate(citations):
        at_least_papers = idx + 1
        print(f"{idx=}, {val=}, {at_least_papers=}")
        if val >= total_len - idx:
            if val >= at_least_papers:
                val = at_least_papers
            if at_least_papers >= val:
                return val

    return 0

if __name__ == "__main__":
    test_case = [
            ([1, 3, 1], 1),
            ([3, 0, 6, 1, 5], 3)
    ]

    for t, a in test_case:
        ans = hIndex(t)
        print(f"Answer: {a}. Result: {ans}")
