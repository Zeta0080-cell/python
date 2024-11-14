def input_student_data():
    """输入单个学生的记录"""
    name = input("请输入学生的姓名: ")
    age = int(input("请输入学生的年龄: "))
    grade = float(input("请输入学生的成绩: "))
    return {"name": name, "age": age, "grade": grade}


def output_student_data(students):
    """输出所有学生的记录"""
    print("\n学生信息：")
    for i, student in enumerate(students, start=1):
        print(f"学生 {i}: 姓名: {student['name']}, 年龄: {student['age']}, 成绩: {student['grade']}")


def main():
    students = []

    # 输入5个学生的数据
    for i in range(5):
        print(f"\n请输入第 {i + 1} 个学生的信息：")
        student = input_student_data()
        students.append(student)

    # 输出所有学生的数据
    output_student_data(students)


if __name__ == "__main__":
    main()