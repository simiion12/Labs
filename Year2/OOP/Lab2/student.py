class Student:
    def __init__(self, first_Name, last_Name, email, enrollment_Date, date_birth):
        self.first_Name = first_Name
        self.last_Name = last_Name
        self.email = email
        self.enrollment_Date = enrollment_Date
        self.date_birth = date_birth

    @staticmethod
    def validate_date(date_str):
        try:
            year, month, day = map(int, date_str.split('/'))

            if not (1 <= month <= 12) or not (1 <= day <= 31):
                raise ValueError("Invalid date format. Please use yyyy/mm/dd.")

            return year, month, day
        except (ValueError, TypeError):
            raise ValueError("Invalid date format. Please use yyyy/mm/dd.")

    def to_dict_as_str(self):
        # Convert the student object to a custom formatted string
        student_str = (
            f'{{First name: {self.first_Name}, '
            f'Last name: {self.last_Name}, '
            f'Email: {self.email}, '
            f'Enrollment date: {self.enrollment_Date}, '
            f'Date of birth: {self.date_birth}}}'
        )
        return student_str

    def add_to_file_enrolled(self, file_name):
        student_info = self.to_dict_as_str()  # Get the student's info as a formatted string

        with open(file_name, 'a') as file:
            file.write(student_info + '\n')


