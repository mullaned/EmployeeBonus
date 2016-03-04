from EmployeePack.Employee import Employee

class Developer(Employee):
    def __init__(self,name,years_worked,language):
        self.language = language
        super(Developer, self).__init__(name,years_worked)

    def calculate_salary(self):
        if self.language == 'python':
            bonus = str(super(Developer,self).calculate_salary() + ((super(Developer,self).calculate_salary())*0.2))
            #return 'Hi %s have worked here for %s years as a developer.  Your salary plus %s bonus is ' %  (self.name,self.years_worked, self.language) + bonus
            return bonus
        else:
            bonus = str(super(Developer,self).calculate_salary() + ((super(Developer,self).calculate_salary())*0.1))
            #return 'Hi %s have worked here for %s years as a developer.  Your salary plus bonus is ' %  (self.name,self.years_worked) + bonus
            return bonus


    def description(self):
        self.salary = super(Developer,self).calculate_salary()
        return 'Hi %s here are your details:\n NAME : %s\n YEARS WORKED: %s\n BASE SALARY: %s\n ROLE: Developer\n LANGUAGE: %s\n' % (self.name,self.name,self.years_worked,self.salary, self.language)


