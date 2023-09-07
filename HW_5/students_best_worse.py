students = {
    'Smith': [7, 9, 10, 10 , 8, 9 , 10],
    'Johns': [10, 3, 8, 10, 7, 9, 9, 9, 10, 10],
    'Cleverly': [8, 1, 9, 8, 8],
    'Johanson': [8, 9, 8, 10, 4, 6]
}

avg_marks = {}
for k, v in students.items():
    avg = sum(v) / len(v)
    avg_marks.update({k: avg})
print(avg_marks)
print('The most successful student is', max(avg_marks, key=avg_marks.get))
print('The least successful student is', min(avg_marks, key=avg_marks.get))
