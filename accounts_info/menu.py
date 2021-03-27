from os import system
import sys
from .trans import trans_edit 
from account_data.accounts_db import account_listing, account_name, account_balance, list_transactions, transaction_list, update_transaction, balance_update
from .account_transact import transact
from .create_delete import create_account, change_account
from .t_edit import tedit_menu, edit_one, edit_two, edit_three, edit_four
from applets.applet import select_transaction
#from .test import select_transaction

save_path = 'bank_accounts/'
information_file = 'information/'


# ? Account List Section
# open the database to get listings

def list_accounts(opt):
    if opt == 'list':
        account_list('list')
    elif opt == 'create':
        account_list('create')
        list_accounts('list')
    elif opt == 'select':
        account_list('select')



def account_list(opt):
    system('clear')
    a_list = account_listing()
    a = 0
    r = 1
    a_list = a_list
    lister(a, r, a_list)
    if opt == 'list':
        list_menu(a, r, a_list)
    elif opt == 'create':
        create_account()
    elif opt == 'select':
        select_menu(a, r, a_list)

# Display the list of accounts
def lister(a, r, a_list):
    #system('clear')
    print('Account List:')
    print()
    b = a + 5
    for r in range(a, b):
        r = r + 1
        if r <= len(a_list):
            print(str(r) + ') ' + a_list[r-1].strip())  
            r = r + 1

# menu for listings of accounts
def list_menu(a, r, a_list):
    print()
    print('List Menu')
    if a + 5 >= len(a_list):
        pass
    else:
        print(' Move down (d) ')
    if a == 0:
        pass
    else:
        print(' Move up (u)')
    print(' Select (s) ')
    print(' Create (c)')
    print(' Delete (a)')
    print(' Edit (e)')
    print(' Exit (q)')
    print()
    choice = input('Select: ')
    if choice == 'q':
        print("\nExiting...")
        sys.exit()
    elif choice == 'd':
        if a + 5 >= len(a_list):
            system('clear')
            lister(a, r, a_list)
            print()
            print('"Enter a correct letter" ')
            list_menu(a, r, a_list)
        else:
            system('clear')
            r = r 
            a = a + 5
            lister(a, r, a_list)
            list_menu(a, r, a_list)
    elif choice == 'u':
        if a != 0:
            system('clear')
            r = r
            a = a - 5
            lister(a, r, a_list)
            list_menu(a, r, a_list)
        else:
            system('clear')
            lister(a, r, a_list)
            print()
            print('"Enter a correct letter" ')
            list_menu(a, r, a_list)
    elif choice == 's':
        r = r
        system('clear')
        lister(a, r, a_list)
        select_menu(a, r, a_list, 'select')
    elif choice == 'c':
        system('clear')
        list_accounts('create')
        list_accounts('list')
    elif choice == 'a':
        system('clear')
        lister(a, r, a_list)
        select_menu(a, r, a_list, 'delete')
    elif choice == 'e':
        system('clear')
        lister(a, r, a_list)
        select_menu(a, r, a_list, 'edit')
    else:
        system('clear')
        lister(a, r, a_list)
        print()
        print('"Enter a correct letter" ')
        list_menu(a, r, a_list)

# select account menu
def select_menu(a, r, a_list, ed_del):
    if a + 5 <= len(a_list):
        high = 0
        pass
    else:
        high = len(a_list) - (a + 5)
    print()
    if ed_del == 'select':
        print('Select Account (' + str(a + 1) + ' - ' + str( a + 5 + high) + ')')
    elif ed_del == 'delete':
        print('Select Account to delete (' + str(a + 1) + ' - ' + str( a + 5 + high) + ')')
    else:
        print('Select Account to edit (' + str(a + 1) + ' - ' + str( a + 5 + high) + ')')
    print('Return (r):')
    print()
    select_account = input('Select account: ')
    system('clear')
    if select_account == 'r':
        system('clear')
        lister(a, r, a_list)
        list_menu(a, r, a_list)
    elif select_account.isnumeric() == False:
        system('clear')
        lister(a, r, a_list)
        print()
        print('"Submit a number or (r)"')
        select_menu(a, r, a_list)
    elif int(select_account) < a + 1 or int(select_account) > (a + 5 + high):
        system('clear')
        lister(a, r, a_list)
        print()
        print('"Submit number within range" ')
        select_menu(a, r, a_list)
    else:
        selected = int(select_account) - 1
        if ed_del == 'select':
            transaction_list(selected, 5)
            page_menu(selected, 5)
        elif ed_del == 'delete':
            lister(a, r, a_list)
            change_account(selected, 'Delete')
            a_list = account_listing()
            lister(a, r, a_list)
            list_menu(a, r, a_list)
        else:
            lister(a, r, a_list)
            change_account(selected, 'Edit')
            a_list = account_listing()
            lister(a, r, a_list)
            list_menu(a, r, a_list)


# The menu under listed transaction
def page_menu(selected, page):
    selected_name = account_name(selected)
    transaction_items = list_transactions(selected_name)
    transaction_len = len(transaction_items) - 1
    print('\nDisplay Menu\n')
    if not int(page) >= transaction_len:
        print(' Page Up (u)')
    if int(page) - 5 > 0:
        print(' Page Down (d)')
    print(' Deposit (a)\n Withdraw (w)\n Edit/Delete Transaction (e)\n Main Menu (m)\n Quit (q)')
    print()
    change = str(input("Select: "))
    change = change.lower()
    if change == "u":
        if not int(page) >= transaction_len:
            system('clear')
            page = str(int(page) + 5)
            transaction_list(selected, page)
            page_menu(selected, page)
        else:
            system('clear')
            transaction_list(selected, page)
            print()
            print('"Selection out of range"')
            page_menu(selected, page)
    elif change == "d":
        if int(page) - 5 > 0:
            system('clear')
            page = str(int(page) - 5)
            print()
            transaction_list(selected, page)
            page_menu(selected, page)
        else:
            system('clear')
            transaction_list(selected, page)
            print()
            print('"Selection out of range"')
            page_menu(selected, page)
    elif change == "e": 
        system('clear')
        transaction_list(selected, page)
        selected_transaction = select_transaction(selected, page)
        if selected_transaction == 'go_back':
            transaction_list(selected, page)
            page_menu(selected, page)
        else:
            system('clear')
            tedit(selected, selected_transaction, page)
    elif change == "a": 
        system('clear')
        transaction_list(selected, page)
        transact(selected, 'Deposit', page)
        transaction_list(selected, page)
        page_menu(selected, page)
    elif change == "w": 
        system('clear')
        transaction_list(selected, page)
        transact(selected, 'Withdraw', page)
        transaction_list(selected, page)
        page_menu(selected, page)
    elif change == "m":
        system('clear')
        account_list('list')
    elif change == "q":
        print("\nExiting...")
        sys.exit()
    else:
        system('clear')
        transaction_list(selected, page)
        print()
        print("Invalid input")
        page_menu(selected, page)

# Select transaction for editing or deleting
#def select_transaction(selected, page):
#    selected_account = account_name(selected)
#    transact_len = list_transactions(selected_account)
#    a = len(transact_len) - (int(page) + 1)
#    b = a + 5
#    if a <= 1:
#        low = a
#    else:
#        low = 0
#    print()
#    print('Select Transaction (' + str(a + 1 - low) + ' - ' + str(a + 5) + ')')
#    print('Return (r):')
#    print()
#    selected_transaction = input('Select: ')
#    system('clear')
#    if selected_transaction == 'r':
#        system('clear')
#        transaction_list(selected, page)
#        page_menu(selected, page)
#    elif selected_transaction.isnumeric() == False:
#        system('clear')
#        transaction_list(selected,page)
#        print()
#        print('"Submit a number or (r)"')
#        select_transaction(selected, page)
#    elif int(selected_transaction) < a + 1 - low or int(selected_transaction) > (a + 5):
#        system('clear')
#        transaction_list(selected, page)
#        print()
#        print('"Submit number within range" ')
#        select_transaction(selected, page, del_ed)
#    else:        
#       #transaction_list(selected, page)
#       # tedit(selected, selected_transaction, page)
#        tedit(selected, selected_transaction, page)
       #else:
       #    trans_edit(selected, selected_transaction, 'Delete', 'transaction', page)
       #transaction_list(selected, page)
       #page_menu(selected, page)


def tedit(selected, selected_transaction, page):
    edit_num = tedit_menu(selected, selected_transaction, page)
    if edit_num == '1':
        system('clear')
        new_date = edit_one(selected, selected_transaction, page)        
        if new_date == 're-edit':
            tedit(selected, selected_transaction, page)
        else:
            selected_account = account_name(selected)
            update_transaction(selected_account, selected_transaction, new_date)
            system('clear')
            tedit(selected, selected_transaction, page)
    elif edit_num == '2':
        system('clear')
        new_tran, new_balance = edit_two(selected, selected_transaction, page)        
        if new_tran == 're-edit':
            tedit(selected, selected_transaction, page)
        else:
            selected_account = account_name(selected)
            update_transaction(selected_account, selected_transaction, new_tran)
            balance_update(selected, new_balance)
            system('clear')
            tedit(selected, selected_transaction, page)
    elif edit_num == '3':
        system('clear')
        new_tran, new_balance = edit_three(selected, selected_transaction, page)        
        if new_tran == 're-edit':
            tedit(selected, selected_transaction, page)
        else:
            selected_account = account_name(selected)
            update_transaction(selected_account, selected_transaction, new_tran)
            balance_update(selected, new_balance)
            system('clear')
            tedit(selected, selected_transaction, page)

    elif edit_num == '4':
        system('clear')
        new_tran, new_balance = edit_four(selected, selected_transaction, page)        
        if new_tran == 're-edit':
            tedit(selected, selected_transaction, page)
        else:
            selected_account = account_name(selected)
            update_transaction(selected_account, selected_transaction, new_tran)
            balance_update(selected, new_balance)
            system('clear')
            tedit(selected, selected_transaction, page)
    else:
        edit_num == '5'
        system('clear')
        transaction_list(selected, page)
        page_menu(selected, page)



#account_list()
