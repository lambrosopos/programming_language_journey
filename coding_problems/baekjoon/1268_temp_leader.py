import sys

N = int(sys.stdin.readline())

classes = []
for _ in range(N):
    class_record = list(map(int, sys.stdin.readline().split()))
    classes.append(class_record)

students_dict = {}
for student_idx, class_record in enumerate(classes):
    for c in class_record:
        if students_dict.get(c) is None:
            students_dict[c] = set([student_idx + 1])
        else:
            students_dict[c].add(student_idx + 1)

student_election = [0 for _ in range(N + 1)]
for key, val in students_dict.items():
    for student_idx in val:
        student_election[student_idx] += 1

print(students_dict)
print(student_election)

