from decimal import Decimal
class comissionEmployee:
    def __init__(self, first_name, last_name, emp_no, rate, sales):
        self._first_name = first_name
        self._last_name = last_name
        self._emp_no = emp_no
        self._rate = rate
        self.sales = sales

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def emp_no(self):
        return self._emp_no

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        if value < Decimal('0.0') or value > Decimal('1.0'):
            raise ValueError('Rate must be between 0.0 and 1.0')
        self._rate = value

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, number_of_sales):
        if number_of_sales < 0:
            raise ValueError('Number of sales must be positive')
        self._sales = number_of_sales

    def earnings(self):
        return self.sales * self.rate

    def __str__(self):
        return f"""
        First name: {self._first_name} 
        Last name: {self._last_name} 
        Phone no: {self._emp_no}
        Comission: {self.earnings()}"""


employee = comissionEmployee('John', 'Smith', 10000, 0.50, 10)
print(employee)
