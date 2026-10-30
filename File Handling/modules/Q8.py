def gross_salary(basic, hra, da):
    return basic + hra + da

def deductions(gross, tax_percent):
    return gross * (tax_percent / 100)

def net_salary(gross, deduction):
    return gross - deduction