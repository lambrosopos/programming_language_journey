total_len = int(input())

def find_print_order(doc_list, doc_idx):
    doc_len = len(doc_list)
    count = 1
    while True:
        largest_num = max(doc_list)
        
        if doc_list[0] == largest_num:
            if doc_idx == 0:
                return count
            else:
                count += 1

            doc_list = doc_list[1:]
            doc_len -= 1
        else:
            doc_list = doc_list[1:] + doc_list[0:1]

        print(f"{doc_len=}, {count=}, {doc_idx=}, {doc_list=}")

        doc_idx = doc_len - 1 if doc_idx == 0 else doc_idx - 1


for i in range(total_len):
    doc_num, doc_idx = map(int, input().split())
    doc_list = list(map(int, input().split()))

    ans = find_print_order(doc_list, doc_idx)
    print(ans)


