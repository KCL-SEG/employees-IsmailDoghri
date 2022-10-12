"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, commission=0, contracts=0):
        self.name = name
        self.commission = commission
        self.contracts = contracts

    def get_pay(self):
        pass

    def __str__(self):
        pass


class MonthlyPaid(Employee):
    def __init__(self, name, monthlySalary, commission=0, contracts=0):
        super().__init__(name, commission, contracts)
        self.monthlySalary = monthlySalary

    def get_pay(self):
        if self.contracts:
            return self.monthlySalary + (self.commission * self.contracts)
        elif self.commission:
            return self.monthlySalary + self.commission
        else:
            return self.monthlySalary

    def __str__(self):
        if self.contracts:
            return str(self.name) + " works on a monthly salary of " + str(self.monthlySalary) + " and receives a commission for " + str(self.contracts) + " contract(s) at " + str(self.commission) + "/contract. Their total pay is " + str(self.get_pay()) + "."
        elif self.commission:
            return str(self.name) + " works on a monthly salary of " + str(self.monthlySalary) + " and receives a bonus commission of " + str(self.commission) + ". Their total pay is " + str(self.get_pay()) + "."
        else:
            return str(self.name) + " works on a monthly salary of " + str(self.monthlySalary) + ". Their total pay is " + str(self.get_pay()) + "."


class HourlyPaid(Employee):
    def __init__(self, name, hourlyWage, hoursWorked, commission=0, contracts=0):
        super().__init__(name, commission, contracts)
        self.hourlyWage = hourlyWage
        self.hoursWorked = hoursWorked

    def get_pay(self):
        if self.contracts:
            return (self.hourlyWage * self.hoursWorked) + (self.commission * self.contracts)
        elif self.commission:
            return (self.hourlyWage * self.hoursWorked) + self.commission
        else:
            return self.hourlyWage * self.hoursWorked

    def __str__(self):
        if self.contracts:
            return str(self.name) + " works on a contract of " + str(self.hoursWorked) + " hours at " + str(self.hourlyWage) + "/hour and receives a commission for " + str(self.contracts) + " contract(s) at " + str(self.commission) + "/contract. Their total pay is " + str(self.get_pay()) + "."
        elif self.commission:
            return str(self.name) + " works on a contract of " + str(self.hoursWorked) + " hours at " + str(self.hourlyWage) + "/hour and receives a bonus commission of " + str(self.commission) + ". Their total pay is " + str(self.get_pay()) + "."
        else:
            return str(self.name) + " works on a contract of " + str(self.hoursWorked) + " hours at " + str(self.hourlyWage) + "/hour. Their total pay is " + str(self.get_pay()) + "."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyPaid('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyPaid('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyPaid('Renee', 3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyPaid('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyPaid('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyPaid('Ariel', 30, 120, 600)
