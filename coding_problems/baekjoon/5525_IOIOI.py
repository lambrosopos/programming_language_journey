import sys

zero_len = int(sys.stdin.readline())
string_len = int(sys.stdin.readline())
string = sys.stdin.readline()


ioi_string = ("IO" * zero_len) + "I"
ioi_len = len(ioi_string)
idx = 0
count = 0

while idx <= (string_len - ioi_len):
    if string[idx] == 'I':
        is_match = True
        for j in range(ioi_len):
            if string[idx + j] != ioi_string[j]:
                if j > 2:
                    idx += j - 1
                is_match = False
                break

        if is_match:
            count += 1

    idx += 1

print(count)

