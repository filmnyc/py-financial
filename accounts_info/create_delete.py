import time
import sys
from os import system, rename, remove
from account_data.accounts_db import account_listing, create_name, new_account, new_balance, account_name, update_account, balance_update

save_path = 'bank_accounts/'
information_file = 'information/'

def create_account():
    print()
    print('Create account name: ')
    print('Return (r):')
    print()
    account_name = input('Name: ')
    if account_name == 'r':
            system('clear')
            return
    print('Opening amount?')
    print('Return (r):')
    print()
    open_amount = input('Amount: $')
    if open_amount == 'r':
            system('clear')
            return
    print()
    open_amount = '{:.2f}'.format(float(open_amount))
    print('New account named ' + account_name + ' with an opening ')
    print('amount of ' + open_amount)
    print()
    opening = ''
    while not opening == 'y' and not opening == 'n':
        opening = input('Add account ' + account_name + '? (y/n) ')
        if opening == 'y' or opening == 'n':
            pass 
        else:
            print('"Create this new account? \'y\' or \'n\'"')
    if opening == 'y':
        pass
    else:
        system('clear')
        return
    create_name(account_name, open_amount)
    #with open(save_path + account_name + ".txt", "w") as f:
        #f.write(account_name + "\n")
        #f.write(time.strftime("%m/%d/%Y") + " account opened - $" + '{:,.2f}'.format(float(open_amount)) + "\n")
    new_account(account_name)
    #with open(information_file + "bankid.txt", "a") as f:
        #f.write(account_name + "\n")   
    new_balance(open_amount)
    #with open(information_file + "balance.txt", "a") as f:
        #f.write(open_amount + '\n')
        #system('clear')
    system('clear')
    return


def change_account(selected, ed_del):
    print()
    selected_name = account_name(selected)
    delete_it = ''
    while not delete_it == 'y' and not delete_it == 'n':
        delete_it = input(ed_del + ' account ' + selected_name + '? (y/n) ')
        if delete_it == 'y' or delete_it == 'n':
            pass 
        else:
            print('"' + ed_del + ' this account? \'y\' or \'n\'"')
    if delete_it == 'y':
        pass
    else:
        system('clear')
        return
    if ed_del == 'Edit':
        print('Change title from ' + selected_name + ' to')
        new_name = input('New title: ')
        rename(save_path + selected_name + '.txt', save_path + new_name + '.txt')
        new_name = new_name + '\n'
        update_account(selected, new_name)
        system('clear')
        return
    else:
        new_name = ''
        update_account(selected, new_name)
        remove(save_path + selected_name + '.txt')
        new_balance = ''
        balance_update(selected, new_balance)
        system('clear')
        return
