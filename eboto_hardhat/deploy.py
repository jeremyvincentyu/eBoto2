from sys import argv
import subprocess
from time import sleep
from os import system
#Start the Hardhat Node
start_node_command = "npx hardhat node"
node_instance = subprocess.Popen(start_node_command.split())
print("Blockchain Started")

sleep(10)

#Erase the old history
erase_history_command = "rm -rf ignition/deployments/chain-31337"
subprocess.run(erase_history_command.split())

#Erase the old election list
erase_list_command = "rm /home/jeremy/Documents/new_eboto/authority_daemon/data/election_list.txt"
system(erase_list_command)

#Erase old control key allocations
erase_controls = "rm -r /home/jeremy/Documents/new_eboto/authority_daemon/data/control_keys/*"
system(erase_controls)

#Erase old dates
erase_dates = "rm -r /home/jeremy/Documents/new_eboto/authority_daemon/data/dates/*"
system(erase_dates)

#Erase old roles
erase_roles ="rm -r /home/jeremy/Documents/new_eboto/authority_daemon/data/roles/*"
system(erase_roles)

#Refill the key pool
refill_command = "cp /home/jeremy/Documents/new_eboto/authority_daemon/data/initial_accounts.json /home/jeremy/Documents/new_eboto/authority_daemon/data/account_pool.json"
system(refill_command)

#Remove the old elections from the isolator
erase_old_elections = "rm -r /home/jeremy/Documents/new_eboto/isolator/data/elections/*"
system(erase_old_elections)

#Remove the old election list from the isolator
erase_old_list = "rm /home/jeremy/Documents/new_eboto/isolator/data/election_list.json"
system(erase_old_list)

#Deploy the contract
deploy_contract_command = f"npx hardhat ignition deploy ignition/modules/{argv[1]} --network localhost"
subprocess.run(deploy_contract_command.split())

print("Contract Deployed")

#Generate the abis
abi_command = "npx solc@0.8.19 --abi contracts/EA_Account.sol"
subprocess.run(abi_command.split())

#Copy the ABI to the frontend
abi_copy_command = "cp contracts_EA_Account_sol_EA_Account.abi /home/jeremy/Documents/new_eboto/eboto_frontend/src/EA_Account.json"
subprocess.run(abi_copy_command.split())

#Copy the ABI to the authority daemon
abi_copy_command = "cp contracts_EA_Account_sol_EA_Account.abi /home/jeremy/Documents/new_eboto/authority_daemon/src/EA_Account.json"
subprocess.run(abi_copy_command.split())

#Copy the ABI to the isolator
abi_copy_command = "cp contracts_EA_Account_sol_EA_Account.abi /home/jeremy/Documents/new_eboto/isolator/src/EA_Account.json"
subprocess.run(abi_copy_command.split())

#Copy the contract address to the frontend
address_copy_command = "cp ignition/deployments/chain-31337/deployed_addresses.json /home/jeremy/Documents/new_eboto/eboto_frontend/src"
subprocess.run(address_copy_command.split())

#Copy the contract address to the authority daemon
address_copy_command = "cp ignition/deployments/chain-31337/deployed_addresses.json /home/jeremy/Documents/new_eboto/authority_daemon/src"
subprocess.run(address_copy_command.split())

#Copy the contract address to the isolator
address_copy_command = "cp ignition/deployments/chain-31337/deployed_addresses.json /home/jeremy/Documents/new_eboto/isolator/src"
subprocess.run(address_copy_command.split())


node_instance.wait()
