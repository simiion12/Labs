from faculty import Faculty


class GeneralOperations:
    def __init__(self, file_name_faculties, file_name_enrolled):
        self.file_name_faculties = file_name_faculties
        self.file_name_enrolled = file_name_enrolled

    def input_faculty(self):
        study_fields = ["Mechanical_Engineering", "Software_Engineering", "Food_Technology", "Urbanism_Architecture",
                        "Veterinary_Medicine"]

        while True:
            Name = input("Enter faculty name: ")
            Abbreviation = input("Enter abbreviation: ")
            print("Available fields: Mechanical_Engineering, Software_Engineering,"
                  " Food_Technology, Urbanism_Architecture, Veterinary_Medicine")
            Study_Field = input("Enter Study_Field: ")
            while Study_Field not in study_fields:
                print("Wrong field, try again")
                Study_Field = input("Enter Study_Field: ")

            try:
                faculty = Faculty(Name, Abbreviation, Study_Field)
                faculty.add_to_file_faculties(self.file_name_faculties)
                print(f"Faculty {Name}, added successfully.")
            except ValueError as e:
                print(e)


            another = input("Do you want to add another faculty? (yes/no): ").lower()
            if another != "yes":
                break

    def search_student_what_faculty(self):
        while True:
            gmail_check = input("Enter the student's email: ")
            student_found = False

            enrolled_students = []  # List to store student information
            faculties_data = []  # List to store faculty information

            # Load enrolled students
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

                    if student["Email"] == gmail_check:
                        student_found = True
                        break

            if not student_found:
                print(f"Student with email '{gmail_check}' not found.")
                continue

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

            faculty_found = False

            # Check if the student is in any faculty
            for faculty in faculties_data:
                if gmail_check in faculty['Student1']:
                    faculty_found = True
                    print(f"Student with email '{gmail_check}' is a member of the following faculty:")
                    print(f"- {faculty['Name']} ({faculty['Abbreviation']})")

            if not faculty_found:
                print(f"Student with email '{gmail_check}' is not found in any faculty.")

            another = input("Do you want to search another student? (yes/no): ").lower()
            if another != "yes":
                break

    def display_faculties(self):
        try:
            with open(self.file_name_faculties, 'r') as faculty_file:
                for line in faculty_file:
                    # Remove extra brackets at the beginning and end
                    line = line.strip()[1:-1]
                    faculty_data = {}
                    # Split the line by commas to separate key-value pairs
                    key_value_pairs = line.strip().split(', ')
                    for pair in key_value_pairs:
                        key, value = pair.split(': ')
                        faculty_data[key] = value
                    print("Name:", faculty_data.get("Name"))
                    print("Abbreviation:", faculty_data.get("Abbreviation"))
                    students_str = faculty_data.get("Student1", "[]")
                    students = [s.strip() for s in students_str.strip("[]").split(';')]
                    print("Students:", students)
                    print("Study Field:", faculty_data.get("Study_Field"))
                    print()

        except FileNotFoundError:
            print(f"The '{self.file_name_faculties}' file does not exist.")

    def display_faculties_by_field(self):
        study_fields = ["Mechanical_Engineering", "Software_Engineering", "Food_Technology", "Urbanism_Architecture",
                        "Veterinary_Medicine"]

        while True:
            print("Available fields: Mechanical_Engineering, Software_Engineering,"
                  " Food_Technology, Urbanism_Architecture, Veterinary_Medicine")
            field = input("Enter the field whose faculties you want to display: ")
            found_field = False
            if field not in study_fields:
                print("Wrong field, try again")
            else:
                try:
                    with open(self.file_name_faculties, 'r') as faculty_file:
                        for line in faculty_file:
                            # Remove extra brackets at the beginning and end
                            line = line.strip()[1:-1]
                            faculty_data = {}
                            # Split the line by commas to separate key-value pairs
                            key_value_pairs = line.strip().split(', ')
                            for pair in key_value_pairs:
                                key, value = pair.split(': ')
                                faculty_data[key] = value
                            if faculty_data["Study_Field"] == field:
                                found_field = True
                                print("Name:", faculty_data.get("Name"))
                                print("Abbreviation:", faculty_data.get("Abbreviation"))
                                students_str = faculty_data.get("Student1", "[]")
                                students = [s.strip() for s in students_str.strip("[]").split(';')]
                                print("Students:", students)
                                print("Study Field:", faculty_data.get("Study_Field"))
                                print()

                    if found_field:
                        break
                    else:
                        print(f"No faculties found in the {field} field")

                except FileNotFoundError:
                    print(f"The '{self.file_name_faculties}' file does not exist.")

            another = input("Do you want to search by another field? (yes/no): ").lower()
            if another != "yes":
                break
