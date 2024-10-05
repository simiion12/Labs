from general_operations import GeneralOperations
from faculty_operations import FacultyOperations
from student_operations import StudentOperations
from student import Student


class University:
    def __init__(self):
        self.file_name_enrolled = "current_enrolled_students.txt"
        self.file_name_faculties = "faculties.txt"
        self.file_name_graduates = "graduated_students.txt"
        self.file_name_congratulation_enrolling = "congratulation_enrolling.txt"
        self.file_name_congratulation_graduating = "congratulation_graduating.txt"
        self.file_name_logging_system = "logging_system.txt"
        self.general_manager = GeneralOperations(self.file_name_faculties, self.file_name_enrolled)
        self.faculty_manager = FacultyOperations(self.file_name_faculties, self.file_name_enrolled,
                                                 self.file_name_graduates, self.file_name_congratulation_enrolling,
                                                 self.file_name_congratulation_graduating)
        self.student_manager = StudentOperations(self.file_name_enrolled, self.file_name_faculties,
                                                 self.file_name_congratulation_enrolling)

    def log_action(self, user_type, current_datetime, action):
        # Create a log entry
        log_entry = f"{current_datetime} - {action} - User Type: {user_type}"

        # Save the log entry to a text file
        with open(self.file_name_logging_system, "a") as log_file:
            log_file.write(log_entry + "\n")

    def run(self):
        print("Welcome to University's student manager system!\n")
        user_type = input("Who is accessing the system now?")
        while True:
            current_datetime = input("Enter current date (yyyy/mm/dd): ")
            try:
                Student.validate_date(current_datetime)
                break
            except ValueError as e:
                print(e)
        print("What do you want to do?\n")
        while True:
            print("g - General operations\n")
            print("f - Faculty operations\n")
            print("s - Student operations\n")
            print("\n")
            print("q - Quit the program")
            choice = input("Enter your choice: ")

            if choice == "g":
                self.log_action(user_type, current_datetime, "Selected General Operations")
                menu_options_g = {
                    1: self.general_manager.input_faculty,
                    2: self.general_manager.search_student_what_faculty,
                    3: self.general_manager.display_faculties,
                    4: self.general_manager.display_faculties_by_field,
                    5: lambda: print("Going back to the previous menu."),
                    6: lambda: (print("Exiting the program.") or exit())
                }

                while True:
                    print("General operations\n")
                    print("What do you want to do ?")
                    print("1 - Create a faculty\n")
                    print("2 - Search what faculty students belong to\n")
                    print("3 - Display university faculties\n")
                    print("4 - Display all faculties belonging to a field\n")
                    print("5 - Back\n")
                    print("6 - Quit the program\n\n")

                    try:
                        choice_g = int(input("Enter your choice: "))
                    except ValueError:
                        print("Invalid input. Please enter a valid numeric choice.")
                        continue

                    if choice_g in menu_options_g:
                        if choice_g == 5 or choice_g == 6:
                            self.log_action(user_type, current_datetime,
                                            f"Selected option {choice_g} from general operations")
                            menu_options_g[choice_g]()  # Execute lambda function
                            break
                        else:
                            self.log_action(user_type, current_datetime,
                                            f"Selected option {choice_g} from general operations")
                            menu_options_g[choice_g]()  # Execute the corresponding method
                    else:
                        print("Invalid choice. Please select a valid option.")

            elif choice == "f":
                self.log_action(user_type, current_datetime, "Selected Faculty Operations")
                menu_options_f = {
                    1: self.faculty_manager.assign_student_to_faculty,
                    2: self.faculty_manager.input_and_assign_student,
                    3: self.faculty_manager.graduate_student,
                    4: self.faculty_manager.display_enrolled_students,
                    5: self.faculty_manager.display_graduated_students,
                    6: lambda: print("Going back to the previous menu."),
                    7: lambda: (print("Exiting the program.") or exit())
                }
                while True:
                    print("Faculty operations\n")
                    print("What do you want to do ?")
                    print("1 - Assign student to a faculty\n")
                    print("2 - Create a student and directly assign to a faculty\n")
                    print("3 - Graduate a student from a faculty\n")
                    print("4 - Display current enrolled students\n")
                    print("5 - Display graduates\n")
                    print("6 - Back\n")
                    print("7 - Quit the program\n")

                    try:
                        choice_f = int(input("Enter your choice: "))
                    except ValueError:
                        print("Invalid input. Please enter a valid numeric choice.")
                        continue

                    if choice_f in menu_options_f:
                        if choice_f == 6 or choice_f == 7:
                            self.log_action(user_type, current_datetime,
                                            f"Selected option {choice_f} from faculty operations")
                            menu_options_f[choice_f]()  # Execute lambda function
                            break
                        else:
                            self.log_action(user_type, current_datetime,
                                            f"Selected option {choice_f} from faculty operations")
                            menu_options_f[choice_f]()  # Execute the corresponding method
                    else:
                        print("Invalid choice. Please select a valid option.")

            elif choice == "s":
                self.log_action(user_type, current_datetime, "Selected Student Operations")
                menu_options_s = {
                    1: self.student_manager.input_student,
                    2: self.student_manager.delete_student_by_email,
                    3: lambda: print("Going back to the previous menu."),
                    4: lambda: (print("Exiting the program.") or exit())
                }
                while True:
                    print("Student operations\n")
                    print("What do you want to do ?")
                    print("1 - Enroll student to university\n")
                    print("2 - Kick student from university\n")
                    print("3 - Back\n")
                    print("4 - Quit the program\n")
                    try:
                        choice_s = int(input("Enter your choice: "))
                    except ValueError:
                        print("Invalid input. Please enter a valid numeric choice.")
                        continue

                    if choice_s in menu_options_s:
                        if choice_s == 3 or choice_s == 4:
                            self.log_action(user_type, current_datetime,
                                            f"Selected option {choice_s} from student operations")
                            menu_options_s[choice_s]()  # Execute lambda function
                            break
                        else:
                            self.log_action(user_type, current_datetime,
                                            f"Selected option {choice_s} from student operations")
                            menu_options_s[choice_s]()  # Execute the corresponding method
                    else:
                        print("Invalid choice. Please select a valid option.")

            elif choice == "q":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    uni = University()
    uni.run()
