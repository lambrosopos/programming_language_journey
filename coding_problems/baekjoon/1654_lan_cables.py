cable_count, target_count = map(int, input().split())

lan_cables = [0] * cable_count
for i in range(cable_count):
    lan_cables[i] = int(input())

lan_cables.sort()

def get_lan_count(length: int):
    count = 0
    for cable in lan_cables:
        count += cable // length

    return count

ans = 0
def longest_lan(low, high):
    global target_count, ans
    if high < low:
        return
    mid = (low + high) // 2
    lan_count = get_lan_count(mid)

    if lan_count >= target_count:
        ans = mid
        longest_lan(mid + 1, high)
    else:
        longest_lan(low, mid - 1)

    


# If number of cables needed is the same to number of lan cables at hand, return the smallest unit
longest_lan(0, lan_cables[-1] * 2)
print(ans)
