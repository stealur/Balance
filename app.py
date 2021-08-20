import data

MENU_PROMPT = """-- Simple Accounts App --

Please choose one of these options:

1) Add a new transaction.
2) See all transactions.
3) Find all transactions by vendor.
4) Find total for one account.
5) Get account totals.
6) Get total for one category.
7) Get category totals.
8) Get monthly spending report.
9) Exit.

Your selection: """

def menu():
    connection = data.connect()
    data.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "9":
        # Menu option 1: Enter in a new transaction
        if user_input == "1":
            date = input("Enter date of transaction: ")
            vendor = input("Enter vendor: ")
            amount = input("Enter amount: ").strip('$')
            amount = int((float(amount))*100)
            account = input("Enter account: ")
            category = input("Enter category: ")

            data.add_transaction(connection, date, vendor, amount, account, category)

        # Menu option 2: Get a list of all transactions
        elif user_input == "2":
            transactions = data.get_all_transactions(connection)

            for transaction in transactions:
                amt = transaction[3]/100
                amt = "{:.2f}".format(amt)
                print(f"{transaction[1]} ({transaction[2]}) - ${amt}")

        # Menu option 3: Find transactions by vendor
        elif user_input == "3":
            vendor = input("Enter name of vendor to find: ")
            transactions = data.get_transactions_by_vendor(connection, vendor)

            for transaction in transactions:
                amt = transaction[3]/100
                amt = "{:.2f}".format(amt)
                print(f"{transaction[1]} ({transaction[2]}) - ${amt}")

        # Menu option 4: Find total by account
        elif user_input == "4":
            account = input("Enter name of account: ")
            total = data.get_total_by_account(connection, account)[0][1]
            total = total/100
            total = "{:.2f}".format(total)
            print(f"${total}")

        # Menu option 5: Find totals for all accounts
        elif user_input == "5":
            totals = data.get_totals_by_account(connection)

            for total in totals:
                formatted_total = total[1]/100
                formatted_total = "{:.2f}".format(formatted_total)
                print(f"{total[0]} - ${formatted_total}")

        # Menu option 6: Find total by category
        elif user_input == "6":
            run = True
            while run:
                category = input("Enter name of category: ")
                if data.is_category_valid(category):
                    total = data.get_total_by_category(connection, category)
 
                    if len(total) != 0:
                        total = total[0][1]
                    else:
                        total = 0
                    total = total/100
                    total = "{:.2f}".format(total)
                    print(f"${total}")
                    run = False
                else:
                    print("Please enter valid shit.")

        # Menu option 7: Find totals for all categories
        elif user_input == "7":
            totals = data.get_totals_by_category(connection)

            for total in totals:
                formatted_total = total[1]/100
                formatted_total = "{:.2f}".format(formatted_total)
                print(f"{total[0]} - ${formatted_total}")

        # Menu option 8: Create monthly report
        elif user_input == "8":
            pass


        else:
            print("Invalid input, please try again!")

menu()

