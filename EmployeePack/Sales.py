from EmployeePack.Employee import Employee


class Sales(Employee):
    def __init__(self,name,years_worked,teritory):
        self.teritory = teritory
        super(Sales, self).__init__(name,years_worked)

    def calculate_salary(self):
        if self.teritory == 'Dublin':
            bonus = str(super(Sales,self).calculate_salary() + ((super(Sales,self).calculate_salary())*0.2))
            #return 'Hi %s you have worked here for %s years in Sales.  Your salary plus %s bonus is ' %  (self.name,self.years_worked, self.teritory) + bonus
            return bonus
        else:
            bonus = str(super(Sales,self).calculate_salary() + ((super(Sales,self).calculate_salary())*0.1))
            #return 'Hi %s you have worked here for %s years in Sales.  Your salary plus bonus is ' %  (self.name,self.years_worked) + bonus
            return bonus

    def description(self):
        return 'Hi %s here are your details:\n NAME : %s\n YEARS WORKED: %s\n BASE SALARY: %s\n ROLE: Sales\n TERITORY: %s\n' % (self.name,self.name,self.years_worked,self.salary, self.teritory)



