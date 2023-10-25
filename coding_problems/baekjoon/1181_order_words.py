total_len = int(input())

word_list = [""] * total_len

for i in range(total_len):
    word_list[i] = input()

word_list = list(set(word_list))
word_list.sort(key=lambda _: (len(_), _))

for w in word_list:
    print(w)
