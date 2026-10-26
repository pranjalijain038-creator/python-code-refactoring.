def get_marks(subject_number):
    """Ask for marks and validate the input."""
    while True:
        try:
            marks = float(input(f"Enter marks for subject {subject_number} (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    student_name = input("Enter student name: ").strip()

    if not student_name:
        print("Student name cannot be empty.")
        return

    marks1 = get_marks(1)
    marks2 = get_marks(2)
    marks3 = get_marks(3)

    total_marks = marks1 + marks2 + marks3
    average_marks = total_marks / 3

    print("\n--- Student Result ---")
    print("Student:", student_name)
    print("Total marks:", total_marks)
    print("Average marks:", round(average_marks, 2))


if __name__ == "__main__":
    main()

