from class_task.classtask import comissionEmployee
from decimal import Decimal


class salaryEmployee(comissionEmployee):
    def __init__(self, first_name, last_name, phone_no, sales, rate, base_salary):
        super().__init__(first_name, last_name, phone_no, sales, rate)
        self._base_salary = base_salary

    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, amount):
        if amount < Decimal('0.00'):
            raise ValueError('Amount cannot be negative')
        self._base_salary = amount

    def earnings(self):
        return self.base_salary + super().earnings()

    def __str__(self):
        return f"""
        {super().__str__()}
        Earnings:{self.earnings()}"""


salary_earner = salaryEmployee('smart', 'ejiofo', 50000, 100, 0.60, 200000)
print(salary_earner)
