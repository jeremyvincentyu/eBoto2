from os import system

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
system(erase_old_elections)

#Remove the old election list from the isolator
erase_old_list = "rm isolator/data/election_list.json"
system(erase_old_list)

#Reset Geth using start.py
reset_geth_command = "bash reset_geth.sh"
system(reset_geth_command)