from student import Student
from faculty_operations import FacultyOperations
class StudentOperations:
    def __init__(self, file_name_enrolled, file_name_faculties, file_name_congratulation_enrolling):
        self.file_name_enrolled = file_name_enrolled
        self.file_name_faculties = file_name_faculties
        self.file_name_congratulation_enrolling = file_name_congratulation_enrolling


    def input_student(self):
        while True:
            first_Name = input("Enter first name: ")
            last_Name = input("Enter last name: ")
            email = input("Enter email: ")

            # Validate enrollment date and date of birth
            while True:
                enrollment_Date = input("Enter enrollment date (yyyy/mm/dd): ")
                try:
                    Student.validate_date(enrollment_Date)
                    break
                except ValueError as e:
                    print(e)

            while True:
                # Check date format
                date_birth = input("Enter date of birth (yyyy/mm/dd): ")
                try:
                    Student.validate_date(date_birth)
                    break
                except ValueError as e:
                    print(e)

            try:
                student = Student(first_Name, last_Name, email, enrollment_Date, date_birth)
                student.add_to_file_enrolled(self.file_name_enrolled)
                print(f"Student {first_Name}, added successfully.")
            except ValueError as e:
                print(e)

            FacultyOperations.congratulations_enrolled(first_Name, last_Name, "", enrollment_Date, self.file_name_congratulation_enrolling)

            another = input("Do you want to add another student? (yes/no): ").lower()
            if another != "yes":
                break

    def delete_student_by_email(self):
        while True:
            kicked_email = input("Input email of which student you want to kick:")

            # Check student existence
            student_found = False
            enrolled_students = []

            with open(self.file_name_enrolled, 'r') as enrolled_file:
                for line in enrolled_file:
                    student_info = line.strip().split(', ')
                    student = {
                        'First name': student_info[0].split(': ')[1],
                        'Last name': student_info[1].split(': ')[1],
                        'Email': student_info[2].split(': ')[1],
                        'Enrollment date': student_info[3].split(': ')[1],
                        'Date of birth': student_info[4].split(': ')[1]
                    }
                    enrolled_students.append(student)

                    if student["Email"] == kicked_email:
                        student_found = True

            if not student_found:
                print(f"Student with email '{kicked_email}' not found.")
                continue

            # Remove the kicked student from the list of enrolled students
            updated_enrolled_students = [student for student in enrolled_students if
                                         student['Email'] != kicked_email]

            # Save the updated list back to current_enrolled_students.txt
            with open(self.file_name_enrolled, 'w') as enrolled_file:
                for student in updated_enrolled_students:
                    enrolled_file.write(
                        f"{{First name: {student['First name']}, Last name: {student['Last name']}, Email: {student['Email']}, Enrollment date: {student['Enrollment date']}, Date of birth: {student['Date of birth']}\n")

            faculties_data = []  # List to store faculty information
            # Load faculty data
            with open(self.file_name_faculties, 'r') as faculty_file:
                for line in faculty_file:
                    faculty_info = line.strip().split(', ')
                    if len(faculty_info) < 4:
                        print("Invalid data in faculties.txt. Please check the file format.")
                        break
                    student1_data = faculty_info[2].split(': ')[1].strip('[]')
                    student1_list = [s.strip() for s in student1_data.split(';') if s.strip()]
                    faculty = {
                        'Name': faculty_info[0].split(': ')[1],
                        'Abbreviation': faculty_info[1].split(': ')[1],
                        'Student1': student1_list,
                        'Study_Field': faculty_info[3].split(': ')[1]
                    }
                    faculties_data.append(faculty)

            # Save the updated faculties data back to faculties.txt
            with open(self.file_name_faculties, 'w') as faculty_file:
                # Iterate through faculties and remove the kicked student from their lists
                for faculty in faculties_data:
                    if kicked_email in faculty.get("Student1", []):
                        faculty["Student1"].remove(kicked_email)
                    students_str = '; '.join(faculty['Student1'])
                    faculty_file.write(
                        f"{{Name: {faculty['Name']}, Abbreviation: {faculty['Abbreviation']}, Student1: [{students_str}], Study_Field: {faculty['Study_Field']}\n")

            print(f"Student with email {kicked_email}, was kicked successfully")
            another = input("Do you want to kick another student? (yes/no): ").lower()
            if another != "yes":
                break

