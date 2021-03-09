from account_data.accounts_db import account_name, list_transactions, transaction_list
import re


# Check for "yes" or "no" action=comment(what you want to do), entity=on a variable, selectedname on object.
def while_yn(action, entity, selected_name):
    transact_it = ''
    while not transact_it == 'y' and not transact_it == 'n':
        print()
        transact_it = input(action + ' ' + entity + ' - ' + selected_name + '? (y/n) ')
        if transact_it == 'y' or transact_it == 'n':
            pass 
        else:
            print()
            print('"' + action + ' ' + entity + '? \'y\' or \'n\'"')
    return transact_it    

# Currancy check for Create Account, Withdraw/Deposit, Edit Transaction
def currency(show):
    message = ''
    while show == 'y':
        print(message)
        amount = input('Amount: $')
        if amount.replace('.', '', 1).isdigit() == False:
            message = '\n "The amount must be in digits"'
            show = 'y'
        elif '.' not in amount:
            new_amount = '{:.2f}'.format(float(amount))
            show = 'n'
            return new_amount
        else:
            d_cents = amount.split('.')
            if len(d_cents[1]) > 2:
                message = '\n"Amount should be formated as currency"'
                show = 'y'
            else:
                new_amount = '{:.2f}'.format(float(amount))
                show = 'n'
                return new_amount


# 'yes' and 'no' function
def go_ahead(statement):
    approve_it = ''
    while not approve_it == 'y' and not approve_it == 'n':
        print()
        approve_it = input(statement + ' (y/n) ')
        if approve_it == 'y' or approve_it == 'n':
            pass 
        else:
            print()
            print('"' + statement + '? \'y\' or \'n\'"')
    return approve_it    

def trans_header(selected, selected_transaction, page):
    selected_account = account_name(selected)

        #Open selected account
    transact_item = list_transactions(selected_account)
    tran = transact_item[int(selected_transaction)]
    tran = tran.split(' ')
    if selected_transaction == '1':
        tran_3 = tran[4]
    else:
        tran_3 = tran[3]
    tran_0 = tran[0]
    if selected_transaction == '1':
        tran_1 = 'account opened'
    else:
        tran_1 = tran[1]
    trim = re.compile(r'[^\d.,]+')
    mystring = tran_3
    tran_3 = trim.sub('', mystring)
    
    
    transaction_list(selected, page)
    print()
    print(selected_transaction + ') ' + tran_0 + ' ' + tran_1 + ' - ' + tran_3)
    print()
    return tran_0, tran_1, tran_3
