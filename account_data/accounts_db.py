import time
save_path = 'bank_accounts/'
information_file = './information/'

# list of Accounts
def account_listing():
    with open(information_file + 'bankid.txt', 'r') as f:
        f.display_account = f.readlines()
        replay = f.display_account
        return replay

# Gets the name of the account variable is 'selected_name'
def account_name(selected):
    with open(information_file + 'bankid.txt', 'r') as f:
        f.acct = f.readlines()
        selected_name = f.acct[int(selected)].strip()
        return selected_name

# Balance of account
def account_balance(selected):
    with open(information_file + 'balance.txt', 'r') as f:
        f.balance = f.readlines()
        selected_balance = f.balance[int(selected)].strip()
        return selected_balance

# list all transactions in account
def list_transactions(selected_name):
    with open(save_path + selected_name.strip() + '.txt', 'r+') as f:
        transaction_items = f.readlines()
        return transaction_items
        update_transaction

# Used in edit transaction to change and update balance and used with
# account_transact to update balance after new transaction is added
def balance_update(selected, new_balance):
    with open(information_file + 'balance.txt', 'r+') as f:
        f.balance = f.readlines()
        f.the_balance = f.balance[int(selected)]
        f.seek(0)
        f.balance[int(selected)] = str(new_balance)
        f.write(''.join(f.balance))
        f.truncate()


#Used in edit transactions to update transaction in account and delete transaction
def update_transaction(selected_account, selected_transaction, new_tran):
    with open(save_path + selected_account.strip() + '.txt', 'r+') as f:
        transact_list = f.readlines()
        old_tran = transact_list[int(selected_transaction)]
        f.seek(0)
        transact_list[int(selected_transaction)] = new_tran
        f.write(''.join(transact_list))
        f.truncate()


# Create the list of transactions in the account
def transaction_list(selected, page):
    print('Transactions List:')
    selected_name = account_name(selected)
    print('\t' + selected_name.strip())
    selected_balance = account_balance(selected)
    print('Current balance - $' + '{:,.2f}'.format(float(selected_balance)).strip())
    # Get all the transactionin a list
    transaction_items = list_transactions(selected_name)
    print()
    a = len(transaction_items) - int(page)
    b = a + 5
    if len(transaction_items) > int(page):
        r = a
    else:
        for i in str(int(page) - len(transaction_items)):
            r = 1
    for i in range(a, b):
        if i > 0 and i <= len(transaction_items) - 1:
            print(str(r) + ') ' + transaction_items[i].strip())  
            r = r + 1

def transaction_add(selected, dorw, d_amount):
    selected_name = account_name(selected)
    with open(save_path + selected_name.strip() + ".txt", "a") as f:
        f.write(time.strftime("%m/%d/%Y") + ' ' + dorw + ' - $' + '{:,.2f}'.format(float(d_amount)) + '\n')

def create_name(account_name, open_amount):
    with open(save_path + account_name + ".txt", "w") as f:
        f.write(account_name + "\n")
        f.write(time.strftime("%m/%d/%Y") + " account opened - $" + '{:,.2f}'.format(float(open_amount)) + "\n")

def new_account(account_name):
    with open(information_file + "bankid.txt", "a") as f:
        f.write(account_name + "\n")   

def new_balance(open_amount):
    with open(information_file + "balance.txt", "a") as f:
        f.write(open_amount + '\n')

# Update and delete account name in "change_account"
def update_account(selected, new_name):
    with open(information_file + "bankid.txt", "r+") as f:
        account_list = f.readlines()
        old_account = account_list[int(selected)]
        f.seek(0)
        account_list[int(selected)] = new_name
        f.write(''.join(account_list))
        f.truncate()

# Currancy check for Create Account, Withdraw/Deposit, Edit Transaction
#def currency(amount, title):
#    message = ''
#    if amount.replace('.', '', 1).isdigit() == False:
#        message = '\n "The ' + title + ' must be in digits"\n'
#        show = 'y'
#        return message, message, show
#    elif '.' not in amount:
#        new_amount = '{:.2f}'.format(float(amount))
#        show = 'n'
#        return new_amount, message, show
#    else:
#        d_cents = amount.split('.')
#        if len(d_cents[1]) > 2:
#            message = '\n"' + title + ' should be formated as currency"\n'
#            show = 'y'
#            return message, message, show
#        else:
#            new_amount = '{:.2f}'.format(float(amount))
#            show = 'n'
#            return new_amount, message, show
