def get_student_data():
    """
    Collects student names and marks from the user.
    Returns a list of dictionaries with student info.
    """
    students = []
    num = int(input("Enter number of students: "))
    for _ in range(num):
        name = input("Enter student name: ")
        marks = float(input(f"Enter marks for {name}: "))
        students.append({'name': name, 'marks': marks})
    return students

def calculate_grade(marks):
    """
    Returns the grade based on marks.
    """
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

def display_results(students):
    """
    Displays the student results with grades.
    """
    print("\nStudent Results:")
    print("-" * 30)
    for student in students:
        grade = calculate_grade(student['marks'])
        print(f"Name: {student['name']}\t Marks: {student['marks']}\t Grade: {grade}")
    print("-" * 30)

def average_marks(students):
    """
    Returns the average marks of all students.
    """
    total = sum(student['marks'] for student in students)
    return total / len(students)

def main():
    students = get_student_data()
    display_results(students)
    avg = average_marks(students)
    print(f"\nAverage Marks: {avg:.2f}")

if __name__ == "__main__":
    main()
