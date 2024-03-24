import math

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    listadd = []

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
# print(student_marks)
# print(query_name)
for key, value in student_marks.items():
    if key == query_name:
        listadd = str(value).replace("[", "").replace("]", "").replace(",", "").split(" ")
        numberbeforeround = (float(listadd[0]) + float(listadd[1]) + float(listadd[2])) / 3
        print("{:0.2f}".format(numberbeforeround))