# Create a dictionary of student names as keys and marks as values
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Daisy": 88
}

# Ask the user to input a student's name
name = input("Enter the student's name: ")

# Retrieve and display marks, or show not found message
if name in student_marks:
    print(name + "'s marks:", student_marks[name])
else:
    print("Student not found.")
