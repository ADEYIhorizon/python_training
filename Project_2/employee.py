import typing

#Employee base class
class Employee:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        print(f"The employee's name is {self.name} and his id is {self.id}")

# #instance of Employee
# myObject = Employee("12345", "Hello")


# print(myObject.__str__())
# print(myObject.__repr__())
# print(myObject)

class SalaryEmployee(Employee):
    def __init__(self, id: int, name: str, weekly_salary: float):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id: int, name: str, no_hours: int, hourly_rate: float):
        super().__init__(id, name)
        self.no_hours = no_hours
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hourly_rate * self.no_hours


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id: int, name: str, weekly_salary: float, commission: float ):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed_salary = super().calculate_payroll()
        print(f'fixed salary is {fixed_salary}')
        return fixed_salary + self.commission

        




