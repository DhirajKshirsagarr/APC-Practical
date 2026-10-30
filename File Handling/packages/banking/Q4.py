def deposit(account, amount):
    account["balance"] = account["balance"] + amount
    return account

def withdraw(account, amount):
    account["balance"] = account["balance"] - amount
    return account