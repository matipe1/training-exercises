def average(dictionary, student):
    student_score = dictionary[f'{student}']
    score_sum = 0
    score_amount = 0

    for i in student_score:
        score_sum += i
        score_amount += 1

    return f"The average score of {student} is {score_sum / score_amount:.2f}"


if __name__ == '__main__':
    n = int(input('Amount of students: '))
    student_marks = {}
    print('Name and scores (e.g. Bob 80 50 70): ')
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Query Name: ")

    print(average(student_marks, query_name))