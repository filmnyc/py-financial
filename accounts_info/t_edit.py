
from os import system
import re
from account_data.accounts_db import account_name, list_transactions, account_balance, balance_update, update_transaction, transaction_list
from applets.applet import while_yn, go_ahead, currency, trans_header

information_file = 'information/' 
save_path = 'bank_accounts/'

#selected to find the account and selected_transaction
#for the specific transaction
def tedit_menu(selected, selected_transaction, del_ed, entity, page):
    trans_header(selected, selected_transaction, page)
    ##Get list of accounts
    #selected_account = account_name(selected)

    #    #Open selected account
    #transact_item = list_transactions(selected_account)
    #tran = transact_item[int(selected_transaction)]
    #tran = tran.split(' ')
    #if selected_transaction == '1':
    #    tran_3 = tran[4]
    #else:
    #    tran_3 = tran[3]
    #tran_0 = tran[0]
    #if selected_transaction == '1':
    #    tran_1 = 'account opened'
    #else:
    #    tran_1 = tran[1]
    #trim = re.compile(r'[^\d.,]+')
    #mystring = tran_3
    #tran_3 = trim.sub('', mystring)

    #edit_it = ''
    #while not edit_it == '4':
    #    transaction_list(selected, page)
    #    print()
    #    print(selected_transaction + ') ' + tran_0 + ' ' + tran_1 + ' - ' + tran_3)
    #    print()
    print('Edit Menu')
    print('\n (1) Edit date\n (2) Edit action\n (3) Change Amount\n (4) Delete Transaction\n (5) Return')
    print()
    edit_it = input('Select: ')
    return edit_it

def edit_one(selected, selected_transaction, del_ed, entity, page):
    ##Get list of accounts
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
    t_date = go_ahead('Change Date from ' + tran_0)
    if t_date == 'y':
        print()
        tran_dm = input('Month: ')
        print(tran_dm.zfill(2) + '/')
        tran_dd = input('Day: ')
        print(tran_dm.zfill(2) + '/' + tran_dd.zfill(2) + '/')
        tran_dy = input('Year: ')
        if len(tran_dy) == 4:
            pass
        else:
            print('"Year must be 4 digits"')
            tran_dy = input('Year: ')
        print()
        print('New date: ' + tran_dm.zfill(2) + '/' + tran_dd.zfill(2) + '/' + tran_dy)
        tran_dok = go_ahead('Is this okay?')
        if tran_dok == 'y':
            tran_d = tran_dm.zfill(2) + '/' + tran_dd.zfill(2) + '/' + tran_dy
            new_tran = (tran_d + ' ' + tran_1 + ' - ' + tran_3 + '\n')
            return new_tran
        else:
            system('clear')
            return 're-edit'
    else:
        system('clear')
        return 're-edit'


def edit_two(selected, selected_transaction, del_ed, entity, page):
    tran_0, tran_1, tran_3 = trans_header(selected, selected_transaction, page)
    if selected_transaction == '1':
        tran_t = 'account opened'
    else:
        if tran_1 == 'Deposit':
            tran_new = 'Withdraw'
        else:
            tran_new = 'Deposit'
    tran_yn = go_ahead('Change ' + tran_1 + ' to ' + tran_new)
    if tran_yn == 'y':
        tran_t = tran_new
        if tran_t == 'Deposit':
            tran_a = tran_3
            tran_total = float(tran_3) + float(tran_a)
            sign = '+'
        else:
            tran_t == 'Withdraw'
            tran_a = tran_3
            tran_total = float(tran_3) + float(tran_a)
            sign = '-'
            tran_a = '${:,.2f}'.format(float(tran_a)) 

            #Compare old transaction to new transaction 
        print()
        print('Original transaction: ' + selected_transaction + ') ' + tran_0 + ' ' + tran_1 + ' - $' + tran_3)
        print('New transaction: ' + selected_transaction + ') ' + tran_0 + ' ' + tran_t + ' - ' + tran_a)
        new_tran = (tran_0 + ' ' + tran_t + ' - ' + tran_a + '\n')

        tran_total = '{:,.2f}'.format(float(tran_total)) 
        print()

        #Alter balance
        print('Alter balance: ' + sign + tran_total)
        tran_total = (sign + tran_total)
        do_trans = go_ahead("If this is okay enter 'y/n': ")
        if do_trans == 'y':
                #show old and new balance
            selected_balance = account_balance(selected)
            old_balance = selected_balance.strip() 
            new_balance = str(float(old_balance) + float(tran_total))
            new_balance = '{:.2f}'.format(float(new_balance)) + '\n'
            print()
            print('Previous balance: ' + old_balance + ' New balance: ' + new_balance)
            do_bal = go_ahead("If this is okay enter 'y/n': ")
            if do_bal == 'y':
                return new_tran, new_balance
                #update balance
                #system('clear')
                #balance_update(selected, new_balance)

                #    #  update transaction record
                #update_transaction(selected_account, selected_transaction, new_tran)
                #trans_edit(selected, selected_transaction, del_ed, entity, page)
            else:
                system('clear')
                return 're-edit', 're-edit'
        else:
            system('clear')
            return 're-edit', 're-edit'
    else:
        system('clear')
        return 're-edit', 're-edit'



def edit_three(selected, selected_transaction, del_ed, entity, page):
    tran_0, tran_1, tran_3 = trans_header(selected, selected_transaction, page)
    change_amt = go_ahead('Change amount of ' + tran_1 + ' from ' + tran_3 + '? ')
    if change_amt == 'y':
        tran_a = currency('y')
    else:
        system('clear')
        return 're-edit', 're-edit'
    
    new_tran = (tran_0 + ' ' + tran_1 + ' - ' + tran_a + '\n')
    print(new_tran)
    do_it = go_ahead('Submit this new transaction? ')
    if do_it == 'y':
        if selected_transaction == '1':
            if float(tran_a) > float(tran_3):
                tran_total = float(tran_a) - float(tran_3)
                sign = '+'
            else:
                tran_total = float(tran_3) - float(tran_a)
                sign = '-'
        else:
            if tran_1 == 'Deposit' and float(tran_3) > float(tran_a):
                tran_total = float(tran_3) - float(tran_a)
                sign = '-'
            elif tran_1 == 'Withdraw' and float(tran_3) > float(tran_a):
                tran_total = float(tran_3) - float(tran_a)
                sign = '+'
            elif tran_1 == 'Deposit' and float(tran_a) > float(tran_3):
                tran_total = float(tran_a) - float(tran_3)
                sign = '+'
            else:
                tran_1 == 'Withdraw' and float(tran_a) > float(tran_3)
                tran_total = float(tran_a) - float(tran_3)
                sign = '-'
    else:
        system('clear')
        return 're-edit', 're-edit'

    tran_a = '${:,.2f}'.format(float(tran_a)) 

    #Compare old transaction to new transaction 
    print()
    print('Original transaction: ' + selected_transaction + ') ' + tran_0 + ' ' + tran_1 + ' - $' + tran_3)
    print('New transaction: ' + selected_transaction + ') ' + tran_0 + ' ' + tran_1 + ' - ' + tran_a)
    new_tran = (tran_0 + ' ' + tran_1 + ' - ' + tran_a + '\n')

    tran_total = '{:,.2f}'.format(float(tran_total)) 
    print()

    #Alter balance
    print('Alter balance: ' + sign + tran_total)
    tran_total = (sign + tran_total)
    do_trans = go_ahead("If this is okay enter 'y/n': ")
    if do_trans == 'y':
        pass
    else:
        system('clear')
        return 're-edit', 're-edit'

        #show old and new balance
    selected_balance = account_balance(selected)
    old_balance = selected_balance.strip() 
    new_balance = str(float(old_balance) + float(tran_total))
    new_balance = '{:.2f}'.format(float(new_balance)) + '\n'
    print()
    print('Previous balance: ' + old_balance + ' New balance: ' + new_balance)
    do_bal = go_ahead("If this is okay enter 'y/n': ")
    if do_bal == 'y':
        return new_tran, new_balance
       # #update balance
       # system('clear')
       # balance_update(selected, new_balance)

       #     #  update transaction record
       # update_transaction(selected_account, selected_transaction, new_tran)
       # trans_edit(selected, selected_transaction, del_ed, entity, page)
    else:
        system('clear')
        return 're-edit', 're-edit'


def edit_four(selected, selected_transaction, del_ed, entity, page):
    tran_0, tran_1, tran_3 = trans_header(selected, selected_transaction, page)
    delete_it = go_ahead('Delete this transaction?')
    if delete_it == 'y':
        tran_total = tran_3
        new_tran = ''
        if tran_1 == 'Deposit':
            sign = '-'
        else:
            sign = '+'

        tran_total = '{:,.2f}'.format(float(tran_total)) 
        print()

        #Alter balance
        print('Alter balance: ' + sign + tran_total)
        tran_total = (sign + tran_total)
        do_trans = go_ahead("If this is okay enter 'y/n': ")
        if do_trans == 'y':
            pass
        else:
            system('clear')
            return 're-edit', 're-edit'

            #show old and new balance
        selected_balance = account_balance(selected)
        old_balance = selected_balance.strip() 
        new_balance = str(float(old_balance) + float(tran_total))
        new_balance = '{:.2f}'.format(float(new_balance)) + '\n'
        print()
        print('Previous balance: ' + old_balance + ' New balance: ' + new_balance)
        do_bal = go_ahead("If this is okay enter 'y/n': ")
        if do_bal == 'y':
            return new_tran, new_balance
        else:
            system('clear')
            return 're-edit', 're-edit'
    
    else:
        system('clear')
        return 're-edit', 're-edit'


