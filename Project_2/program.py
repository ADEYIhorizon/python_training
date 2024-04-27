from employee import SalaryEmployee, HourlyEmployee, CommissionEmployee
# from payroll import PayrollSystem as payroll_system 
import payroll



salary_employee = SalaryEmployee(1, "Salary Employee", 25020)
hourly_employee = HourlyEmployee(1, "Salary Employee", 2, 2500)
commission_employee = CommissionEmployee(1, "Salary Employee", 25020, 2500)

# print(salary_employee.calculate_payroll())

# print(payroll_system)

payroll_system =  payroll.PayrollSystem()
payroll_system.calculate_payroll(
    [salary_employee, hourly_employee, commission_employee]
)