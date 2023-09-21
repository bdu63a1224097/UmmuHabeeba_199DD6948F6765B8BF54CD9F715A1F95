class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the student list based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:
if __name__ == "__main__":
    # Create a list of student objects
    students = [
        Student("Ravi", "A001", 3.9),
        Student("Mahesh", "B002", 3.7),
        Student("Chandran", "C003", 3.5),
        Student("Kumar", "D004", 3.8),
    ]

    # Sort the students by CGPA
    sorted_students = sort_students(students)

    # Print the sorted list of students
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
      
