import random
import sys

account = []


def first_name():
    user_first_name = input("Enter your first name: ")
    return user_first_name


def last_name():
    user_last_name = input("Enter your last name: ")
    return user_last_name


def amount_collector():
    user_amount = int(input("Enter amount: "))
    return user_amount


def acct_number_collector():
    user_amount = int(input("Enter account: "))
    return user_amount


def phone_no():
    user_phone_no = input("Enter your phone number: ")
    return user_phone_no


def pin():
    user_pin = input("Enter your pin: ")
    return user_pin


def generate_account_number():
    return random.randint(000000, 999999)


balance = 0.0


def prompt():
    return """  
Please choose an option:
1. Create a new account
2. Deposit money
3. Withdraw money
4. Transfer money
5. Change pin
6. Check balance
7. Exit"""


def main():
    print(prompt())
    selected_option = input("Enter your option: ")
    match selected_option:
        case "1":
            account_creator()
            prompt()
            main()
        case "2":
            user_pin = pin()
            amount = amount_collector()
            deposit_money(user_pin, amount)
            prompt()
            main()
        case "3":
            user_pin = pin()
            amount = amount_collector()
            withdraw_money(user_pin, amount)
            prompt()
            main()
        case "4":
            user_pin = pin()
            amount = amount_collector()
            acct_no = acct_number_collector()
            transfer_money(user_pin, acct_no, amount)
            prompt()
            main()
        case "5":
            old_pin = pin()
            change_pin(old_pin)
            prompt()
            main()
        case "6":
            user_pin = pin()
            check_balance(user_pin)
            main()
        case "7":
            end_program()


def account_creator():
    first_name1 = input("Enter your first name: ")
    last_name1 = input("Enter your last name: ")
    phone_number = input("Enter your phone number: ")
    initial_pin = input("Enter your pin: ")
    account_number = generate_account_number()
    account.append([first_name1, last_name1, phone_number, initial_pin, account_number, balance])
    for element in account:
        print(element)
        print()


def deposit_money(user_pin, amount):
    for element in account:
        if user_pin == element[3]:
            element[5] += amount
            print("deposited", amount, "naira")
        else:
            continue


def withdraw_money(user_pin, amount):
    for element in account:
        if user_pin == element[3]:
            if element[5] > amount > 0:
                element[5] -= amount
                print("debited", amount, "naira")
                break
            else:
                print("Insufficient balance or amount is negative")
            break
        else:
            continue


def transfer_money(user_pin, acct_no, amount):
    for element in account:
        if user_pin == element[3]:
            if element[5] > amount > 0:
                element[5] -= amount
                print("debited", amount, "naira")
                break
            else:
                print("Insufficient balance or amount is negative")
            break
        else:
            continue

    count = 0
    for index in account:
        if acct_no == index[4]:
            index[5] += amount
            count += 1
            print("Transfer of", amount, "naira to", index[0], index[1], "Successful.")
            break

    if count == 0:
        for element in account:
            if user_pin == element[3]:
                element[5] += amount
            else:
                continue


def change_pin(old_pin):
    for element in account:
        if old_pin == element[3]:
            element[3] = pin()
            return "New pin set....."


def check_balance(user_pin):
    for element in account:
        if user_pin == element[3]:
            print(element)
            break


def end_program():
    print("Thank you for choosing Sunday-fast-pay services")
    sys.exit(0)


print("""
====================================
WELCOME TO SUNDAY-FAST-PAY BANK SERVICES
====================================""")

print(main())
