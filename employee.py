class Employee:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

	def fullname(self):
		return f"{self.firstname.capitalize()} {self.lastname.capitalize()}"

	def email(self):
		return f"{self.firstname.lower()}.{self.lastname.lower()}@company.com"

	def firstname(self):
		return f"{self.firstname}"
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")

print(emp_1.fullname())
print(emp_2.email())
print(emp_3.firstname)