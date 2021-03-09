#from os import system
#import math
#import sys
#import time
##from accounts_info.trans import trans_edit
from accounts_info.menu import list_accounts
#information_file = 'information/'
#save_path = 'bank_accounts/'

#print(__name__)

def main():
    opt = 'list'
    list_accounts(opt)
    

if __name__ == "__main__":
    # execute only if run as a script
    main()    
    
    
    #with open(information_file + 'bankid.txt', 'r') as f:
        #f.display_account = f.readlines()
        #a_list = f.display_account
        #print()
        #a = 0
        #r = 1
        #a_list = a_list
        #lister(a, r, a_list)




        #list_menu(a, r, a_list)



    #account_list()


#main()
