import time

class Solution:
    def jump(self, nums: list[int]) -> int:
        total_len = len(nums)
        min_jumps = [-1] * total_len

        def do_jump(idx: int, total_jumps: int, min_jumps: list[int]):
            # Current idx, keep track of total jumps
            if min_jumps[idx] == -1 or total_jumps <= min_jumps[idx]:
                min_jumps[idx] = total_jumps

            if min_jumps[idx] != -1 and min_jumps[idx] < total_jumps:
                return
                

            for step in range(1, nums[idx] + 1):
                if idx + step >= total_len:
                    continue

                do_jump(idx + step, total_jumps + 1, min_jumps)

        do_jump(0, 0, min_jumps)
        # print(min_jumps)
        return min_jumps[-1]

sol = Solution()

test_cases = [
[5,8,1,8,9,8,7,1,7,5,8,6,5,4,7,3,9,9,0,6,6,3,4,8,0,5,8,9,5,3,7,2,1,8,2,3,8,9,4,7,6,2,5,2,8,2,7,9,3,7,6,9,2,0,8,2,7,8,4,4,1,1,6,4,1,0,7,2,0,3,9,8,7,7,0,6,9,9,7,3,6,3,4,8,6,4,3,3,2,7,8,5,8,6,0]
]

start = time.time()
ans = sol.jump(test_cases[0])
end = time.time()

print("Time:", end - start)
print(ans)
