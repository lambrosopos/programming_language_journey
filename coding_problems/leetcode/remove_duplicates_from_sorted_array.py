def removeDuplicates(nums):
    for idx, val in enumerate(nums):
        if idx == len(nums) - 1:
            break

        while nums[idx + 1] == val:
            del nums[idx + 1]

    return nums

if __name__ == "__main__":
    l1 = [1, 1, 2]
    print(removeDuplicates(l1))
