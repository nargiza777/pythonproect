class Employee:
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = "{}.{}@company.com".format(first,last)
        self.pay = pay
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
class Developer(Employee):
    raise_amt = 1.10
    def __init__(self,first,last,pay,prog_language):
        super().__init__(first,last,pay)
        self.prog_language = prog_language
class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print("name is ",emp.fullname())

dev_1 = Developer("Memis","Cetinkaya",10000,"Ruby")
dev_2 = Developer("Mark","Tagatz",10000,"Ruby")
dev_3 = Developer("Bonnie","Moore",50000,"Java")
print(dev_1.pay)
print(dev_1.email)
dev_1.apply_raise()
print(dev_1.pay)

mgr= Manager ("Jamie","Diamon",60000,[dev_1,dev_2,dev_3])
mgr2= Manager ("Jimmy","Johnson",15000)


#mgr.add_emp(dev_2)
#mgr.add_emp(dev_3)
mgr.print_emps()
print("----Before-removing")
mgr.remove_emp(dev_1)
mgr.print_emps()
print("--Printing mgr2.print_emps()--")
mgr2.print_emps()
# emp = Employee("Memis","Cetinkaya",10000)
# print(emp.email)
# print(emp.fullname())
# print(emp.pay)
# emp.apply_raise()
# print(emp.pay)