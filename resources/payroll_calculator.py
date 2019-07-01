class Employee:
    basic_salary = 0
    benefits = 0
    net_salary = 0
    payee = 0
    nhif= 0
    nssf = 0
    gross_salary = 0


    #constructor
    def __init__(self,basic_sal,benefit):
        self.basic_salary=basic_sal
        self.benefits=benefit
        self.calc_payee()
        self.calc_NHIF()
        self.calc_Nssf()
        self.calc_gross_salary()
        self.calc_net_salary()


    #Calculating paye tax
    def calc_payee(self):
        taxable_pay = self.gross_salary - self.nssf
        if taxable_pay >= 0 and taxable_pay <= 12298:
            self.payee = 0.1 * taxable_pay
            return self.payee
        elif taxable_pay >= 12299 and taxable_pay <= 23885:
            tax_amount1 = 0.1 * 12298
            tax_amount2 = 0.15 * (taxable_pay - 12298)
            self.payee = tax_amount1 + tax_amount2
            return self.payee
        elif taxable_pay >= 23886 and taxable_pay <= 35472:
            tax_amount1 = 0.1 * 12298
            tax_amount2 = 0.15 * 11587
            tax_amount3 = 0.2 * (taxable_pay-23885)
            self.payee = tax_amount1 + tax_amount2 + tax_amount3
            return self.payee
        elif taxable_pay >=35473 and taxable_pay <= 47059:
            tax_amount1 = 0.1 * 12298
            tax_amount2 = 0.15 * 11587
            tax_amount3 = 0.2 * 11587
            tax_amount4 = 0.25 * (taxable_pay-35472)
            self.payee = tax_amount1 + tax_amount2 + tax_amount3 + tax_amount4 + tax_amount4
            return self.payee
        elif taxable_pay > 47059:
            tax_amount1 = 0.1 * 12298
            tax_amount2 = 0.15 * 11587
            tax_amount3 = 0.2 * 11587
            tax_amount4 = 0.25 * 11587
            tax_amount5 = 0.3 * (taxable_pay-47059)
            self.payee = tax_amount1 + tax_amount2 + tax_amount3 + tax_amount4 + tax_amount5
            return self.payee


    #Calculating nhif deduction
    def calc_NHIF(self):
        gross = self.gross_salary
        if gross >= 100000:
            self.nhif = 1700
            return self.nhif
        elif gross >= 90000 and gross <=99999:
            self.nhif = 1600
            return self.nhif
        elif gross >= 80000 and gross <=89999:
            self.nhif = 1500
            return self.nhif
        elif gross >= 80000 and gross <=89999:
            self.nhif = 1500
            return self.nhif
        elif gross >= 70000 and gross <=79999:
            self.nhif = 1400
            return self.nhif
        elif gross >= 60000 and gross <=69999:
            self.nhif = 1300
            return self.nhif
        elif gross >= 50000 and gross <=59999:
            self.nhif = 1200
            return self.nhif
        elif gross >= 45000 and gross <=49999:
            self.nhif = 1100
            return self.nhif
        elif gross >= 40000 and gross <=44999:
            self.nhif = 1000
            return self.nhif
        elif gross >= 35000 and gross <=39999:
            self.nhif = 950
            return self.nhif
        elif gross >= 30000 and gross <=34999:
            self.nhif = 900
            return self.nhif
        elif gross >= 25000 and gross <=29999:
            self.nhif = 850
            return self.nhif
        elif gross >= 20000 and gross <=24999:
            self.nhif = 750
            return self.nhif
        elif gross >= 15000 and gross <=19999:
            self.nhif = 600
            return self.nhif
        elif gross >= 12000 and gross <=14999:
            self.nhif = 500
            return self.nhif
        elif gross >= 8000 and gross <=11999:
            self.nhif = 400
            return self.nhif
        elif gross >= 6000 and gross <=7999:
            self.nhif = 300
            return self.nhif
        else:
            self.nhif=150
            return self.nhif



     #Calculating Nssf deduction
    def calc_Nssf(self):

       if 0.06*float(self.basic_salary) >= 6000:
            self.nssf=6000
            return self.nssf

       else:
            self.nssf = 0.06* float(self.basic_salary)
            return self.nssf

    #Calculating Gross Salary
    def calc_gross_salary(self):
        self.gross_salary = self.basic_salary + self.benefits
        return self.gross_salary

    #Calculating Net Salary
    def calc_net_salary(self):
        self.net_salary = self.gross_salary - self.payee - self.nhif
        return self.net_salary