from os import system
from account_data.accounts_db import account_name, list_transactions, transaction_add, account_balance, balance_update, transaction_list
import time
from applets.applet import currency, while_yn, go_ahead


def transact(selected, dorw, page):
    selected_name = account_name(selected)
    transact_it = while_yn(dorw, 'transaction', selected_name)   
    while not transact_it == 'n':
        print()
        d_amount = input('Amount of ' + dorw + ': $')
        amount = currency(d_amount, dorw)
        if amount[2] == 'y':
             system('clear') 
             transaction_list(selected, page)
             print(amount[1])
             transact_it = while_yn(dorw, 'transaction', selected_name)   
        else:
            print()
            new_transaction = time.strftime("%m/%d/%Y") + ' ' + dorw + ' - $' + amount[0]
            print(new_transaction)
            okay_it = go_ahead("If this is okay enter?")
            #add_it = while_yn(dorw, 'transaction',selected_name)
            if okay_it == 'y':
                pass
            else:
                system('clear')
                return
            old_balance = account_balance(selected)
            old_balance = float(old_balance)
            d_amount = float(d_amount)
            if dorw == 'Deposit':
                new_balance = old_balance + d_amount
            else:
                new_balance = old_balance - d_amount
            new_balance = '{:.2f}'.format(float(new_balance))
            old_balance = '{:.2f}'.format(float(old_balance))
            print()
            print('The existing balance is ' + str(old_balance) + ' and the new balance will be ' + str(new_balance))
            okay_it = go_ahead("If this is okay enter?")
            #okay_it = while_yn(dorw, 'transaction', selected_name)
            if okay_it == 'y':
                new_balance = new_balance + '\n'
                d_amount = str(d_amount)
                transaction_add(selected, dorw, d_amount)
                balance_update(selected, new_balance)
                system('clear')
                return
            else:
                system('clear')
                return
    else:
        system('clear')
        return


#def while_yn(dorw, selected_name):
#    transact_it = ''
#    while not transact_it == 'y' and not transact_it == 'n':
#        transact_it = input('Add a ' + dorw + ' to ' + selected_name + '? (y/n) ')
#        if transact_it == 'y' or transact_it == 'n':
#            pass 
#        else:
#            print('"Make a ' + dorw + '? \'y\' or \'n\'"')
#    return transact_it    

#transact(3, 'Withdraw', 5)
