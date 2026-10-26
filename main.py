
# Student Academic Performance Classifier

# Fixed grade categories stored in a tuple
GRADE_CATEGORIES = ("Excellent", "Good", "Pass", "Fail")

# List of dictionaries to store student records
students = []


# Function to classify grades
def classify_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 80:
        return GRADE_CATEGORIES[0]
    elif score >= 60:
        return GRADE_CATEGORIES[1]
    elif score >= 40:
        return GRADE_CATEGORIES[2]
    else:
        return GRADE_CATEGORIES[3]


# Function to calculate average score
def calculate_average(students):
    if len(students) == 0:
        return 0

    total = 0
    for student in students:
        total += student["python_score"]

    return total / len(students)


# Function to count passing students
def count_passing_students(students):
    count = 0
    for student in students:
        if student["python_score"] >= 40:
            count += 1
    return count


# Function to collect student information
def collect_students():
    number = int(input("Enter number of students: "))

    for i in range(number):
        print(f"\nEnter information for Student {i + 1}")

        name = input("Name: ").strip()
        age = int(input("Age: "))
        study_hours = float(input("Study Hours: "))

        while True:
            try:
                score = float(input("Python Score (0-100): "))

                if 0 <= score <= 100:
                    break
                else:
                    print("Score must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid score.")

        student = {
            "name": name,
            "age": age,
            "study_hours": study_hours,
            "python_score": score
        }

        students.append(student)


# Function to display performance report
def display_report(students):
    print("\n===== STUDENT PERFORMANCE REPORT =====")

    for student in students:
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Study Hours: {student['study_hours']}")
        print(f"Score: {student['python_score']}")
        print(f"Grade: {classify_grade(student['python_score'])}")

    if len(students) == 0:
        print("\nNo student records available.")
        return

    scores = [student["python_score"] for student in students]

    average = calculate_average(students)
    highest = max(scores)
    lowest = min(scores)
    passed = count_passing_students(students)
    failed = len(students) - passed

    top_student = max(
        students,
        key=lambda student: student["python_score"]
    )

    print("\n===== SUMMARY =====")
    print(f"Total Students: {len(students)}")
    print(f"Average Score: {average:.2f}")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")
    print(f"Passed Students: {passed}")
    print(f"Failed Students: {failed}")
    print(f"Top Student: {top_student['name']}")


# Main function
def main():
    collect_students()
    display_report(students)


if __name__ == "__main__":
    main()
