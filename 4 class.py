class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class PayrollSystem:
    def calculate_pay(self, employee):
        if employee.position == 'developer':
            return self.calculate_developer_pay(employee)
        elif employee.position == 'manager':
            return self.calculate_manager_pay(employee)
    
    def calculate_developer_pay(self, employee):
        # Calculate pay for developer
        pass

    def calculate_manager_pay(self, employee):
        # Calculate pay for manager
        pass

class TaxCalculator:
    def calculate_tax(self, employee, salary):
        if employee.position == 'developer':
            return self.calculate_developer_tax(salary)
        elif employee.position == 'manager':
            return self.calculate_manager_tax(salary)
    
    def calculate_developer_tax(self, salary):
        # Calculate tax for developer
        pass

    def calculate_manager_tax(self, salary):
        # Calculate tax for manager
        pass

class HRSystem:
    def __init__(self):
        self.payroll_system = PayrollSystem()
        self.tax_calculator = TaxCalculator()

    def process_employee(self, employee, salary):
        net_pay = self.payroll_system.calculate_pay(employee)
        tax = self.tax_calculator.calculate_tax(employee, salary)
        # Other HR processes