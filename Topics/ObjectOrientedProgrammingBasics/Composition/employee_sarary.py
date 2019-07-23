''' 
The classes have an "Has-A" relationship. The Employee "Has-A" Salary, so we can use the Salary class as a container within the Employee class to add additional functionality.
'''
class Salary: 
  def __init__(self, pay, bonus):
    self.pay = pay
    self.bonus= bonus

  def annual_salary(self):
    return (self.pay*12) + self.bonus


class Employee:
  def __init__(self, name, age, pay, bonus):
    self.name=name
    self.age=age
    self.bonus=bonus
    self.obj_salary=Salary(pay, bonus)
  
  def total_salary(self):
    return self.obj_salary.annual_salary()
    

  def discription(self):
    """
    Prints the employee information

    Returns:
    dic{name,age,salary,bonus}
    """
    employee_json={"name":self.name, "age": self.age, "salary":self.obj_salary.annual_salary(), "bonus":self.bonus}
    return employee_json

emp1 = Employee("Mike", 26, 71000,10000)
print(emp1.discription())