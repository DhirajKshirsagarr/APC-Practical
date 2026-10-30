import salary

basic = 30000
hra = 10000
da = 5000

gross = salary.gross_salary(basic, hra, da)
deduction = salary.deductions(gross, 10)
net = salary.net_salary(gross, deduction)

print("Gross salary =", gross)
print("Deductions =", deduction)
print("Net salary =", net)