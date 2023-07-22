def lowest(array):
    # Variables
    flag = True
    lowest = None

    for student, grade in array:
        if flag:
            lowest = grade
            flag = False

        elif grade < lowest:
            lowest = grade

    return lowest


def second_lowest(student_list):
    # Variables
    lowest_grade = lowest(student_list)
    flag = True
    second_lowest_grade = []

    for student, grade in student_list:
        if not grade == lowest_grade:
            if flag:
                second_lowest_grade.append([student, grade])
                flag = False

            else:
                if second_lowest_grade[0][1] > grade:
                    second_lowest_grade.pop(0)
                    second_lowest_grade.append([student, grade])

                elif second_lowest_grade[0][1] == grade:
                    second_lowest_grade.append([student, grade])

    return second_lowest_grade


def second_lowest_names(second_list):
    # Variables
    student_names = []
    second_lowest_list = second_lowest(second_list)

    for student, grade in second_lowest_list:
        student_names.append(student)

    student_names.sort()

    print(f'The name(s) of the second lowest scorer(s) are the following:')
    for name in student_names:
        print(name)


if __name__ == '__main__':
    array = []
    for i in range(int(input("Cantidad de Alumnos: "))):
        name = input("Nombre: ")
        score = float(input("Nota: "))

        array.append([name, score])

    second_lowest_names(array)
