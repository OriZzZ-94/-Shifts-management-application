

class Employee:
    def __init__(cls, name, num_of_shifts, employee_number):
        cls.employee_number = employee_number
        cls.name = name
        cls.num_of_shifts = num_of_shifts


class Shift:
    def __init__(cls,shift_num, num_of_shifts, list_of_employees):
        cls.shift_num = shift_num
        cls.num_of_shifts = num_of_shifts
        cls.list_of_employees = list_of_employees


