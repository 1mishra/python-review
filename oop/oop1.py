# PYTHON object oriented program

class Employee:
	pass

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'


	def fullname(self):
		return '{} {} '.format(self.first, self.last)

emp_1 = Employee('Jon', 'Snow', 1000000)
emp_2 = Employee('Arya', 'Stark', 500000)


emp_1.fullname()
print(Employee.fullname(emp_1))

print(emp_1.fullname())