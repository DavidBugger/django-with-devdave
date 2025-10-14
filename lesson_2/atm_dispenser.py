


def atm_dispenser(balance, withdraw):
    user_pin = "1234"
    # balance = 5000
    user_input_pin = input("Enter your PIN: ")
    if user_input_pin != user_pin:
        return "Invalid PIN please try again! "
    
    amount_to_withdraw = int(input("Enter amount to withdraw (50, 100, 200, 500, 1000): "))
    
    if amount_to_withdraw > balance:
        return "Insufficient funds"
    else:
        balance -= amount_to_withdraw
        return f"Please take your cash. Your new balance is {balance}"

if __name__ == "__main__":
    print(atm_dispenser(5000))