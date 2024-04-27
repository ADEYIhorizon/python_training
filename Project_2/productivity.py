class ProductivitySystem:
    def track(self, employees, hours):
        print("calculating Payroll")
        print("================================")

        for employee in employees:
            print(f"{employee.name} works for {employee.hours}")
            print("\n") 