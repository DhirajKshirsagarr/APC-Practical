from banking import account, transaction, loan

acc = account.create_account("Rehan", 5000)
acc = transaction.deposit(acc, 2000)
acc = transaction.withdraw(acc, 1000)

print("Balance =", acc["balance"])
print("Loan amount =", loan.calculate_loan(10000, 5, 2))