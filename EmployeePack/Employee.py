class Employee(object):
    def __init__(self,name,years_worked):
        self.name = name
        self.years_worked = years_worked
        self.salary = 5000



    def calculate_salary(self):
        if self.years_worked < 3:
            self.salary = self.salary + (self.salary * 0.1)
            return self.salary

        if self.years_worked <= 5:
            self.salary = self.salary + (self.salary * 0.2)
            return self.salary

        else:
            self.salary = self.salary + (self.salary * 0.25)
            return self.salary


