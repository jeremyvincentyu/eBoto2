from os import system,mkdir

#Erase the old election list
erase_list_command = "rm authority_daemon/data/election_list.txt"
system(erase_list_command)

#Erase old control key allocations
erase_controls = "rm -r authority_daemon/data/control_keys/*"
system(erase_controls)

#Erase old dates
erase_dates = "rm -r authority_daemon/data/dates/*"
system(erase_dates)

#Erase old roles
erase_roles ="rm -r authority_daemon/data/roles/*"
system(erase_roles)

#Refill the key pool
refill_command = "cp authority_daemon/data/initial_accounts.json authority_daemon/data/account_pool.json"
system(refill_command)

#Remove the old elections from the isolator
erase_old_elections = "rm -r isolator/data/elections/*"
try:
    mkdir("isolator/data/elections")
except:
    print("isolator/data/elections already exists")
    
system(erase_old_elections)

#Remove the old election list from the isolator
erase_old_list = "rm isolator/data/election_list.json"
system(erase_old_list)

#Remove the old private keys from the tester
erase_old_keys = "rm -rf testing/data/private_keys && mkdir testing/data/private_keys"
system(erase_old_keys)

#Reset Geth using start.py
reset_geth_command = "bash reset_geth.sh"
system(reset_geth_command)