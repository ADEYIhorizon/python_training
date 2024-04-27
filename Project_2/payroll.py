class PayrollSystem:
    def calculate_payroll(self, employees: any):
        print("calculating Payroll")
        print("================================")

        for employee in employees:
            print(f"payroll for {employee.name}")
            print(f"Salary Amount {employee.calculate_payroll()}")
            print("\n")
