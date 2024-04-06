import subprocess
from time import sleep
from os import kill, system

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


#Start the hardhat first,
hardhat_process = subprocess.Popen("bash hardhat.sh".split(),stdout=subprocess.PIPE, stdin = subprocess.PIPE, stderr=subprocess.PIPE)
sleep(10)
 
#Copy the ABI to the frontend
abi_copy_command = "cp eboto_hardhat/contracts_EA_Account_sol_EA_Account.abi /home/jeremy/Documents/new_eboto/eboto_frontend/src/EA_Account.json"
subprocess.run(abi_copy_command.split())

#Copy the ABI to the authority daemon
abi_copy_command = "cp eboto_hardhat/contracts_EA_Account_sol_EA_Account.abi /home/jeremy/Documents/new_eboto/authority_daemon/src/EA_Account.json"
subprocess.run(abi_copy_command.split())

#Copy the ABI to the isolator
abi_copy_command = "cp eboto_hardhat/contracts_EA_Account_sol_EA_Account.abi /home/jeremy/Documents/new_eboto/isolator/src/EA_Account.json"
subprocess.run(abi_copy_command.split())

#Copy the contract address to the frontend
address_copy_command = "cp eboto_hardhat/ignition/deployments/chain-31337/deployed_addresses.json /home/jeremy/Documents/new_eboto/eboto_frontend/src"
subprocess.run(address_copy_command.split())

#Copy the contract address to the authority daemon
address_copy_command = "cp eboto_hardhat/ignition/deployments/chain-31337/deployed_addresses.json /home/jeremy/Documents/new_eboto/authority_daemon/src"
subprocess.run(address_copy_command.split())

#Copy the contract address to the isolator
address_copy_command = "cp eboto_hardhat/ignition/deployments/chain-31337/deployed_addresses.json /home/jeremy/Documents/new_eboto/isolator/src"
subprocess.run(address_copy_command.split())

#Then start the isolator,
print("Attempting to start isolator")
isolator_process = subprocess.Popen("bash isolator.sh".split(),stdout=subprocess.PIPE, stdin = subprocess.PIPE, stderr=subprocess.PIPE)

# and finally the authority daemon
print("Attempting to start authority daemon")
authority_process = subprocess.Popen("bash authority.sh".split(),stdout=subprocess.PIPE, stdin = subprocess.PIPE, stderr=subprocess.PIPE)

sleep(5)

while True:
    stop_code = input("Input 'stop' to stop all backends.")
    if stop_code.strip() == "stop":
        hardhat_process.kill()
        hardhat_process.wait()
        isolator_process.kill()
        isolator_process.wait()
        authority_process.kill()
        authority_process.wait()
        flask_processes = subprocess.run("ps aux".split(), capture_output=True, universal_newlines=True,text=True)
        flask_lines = flask_processes.stdout.split("\n")
        for every_line in flask_lines:
            if "flask" in every_line or "hardhat node" in every_line:
                line_contents = every_line.split()
                pid = int(line_contents[1])
                print(f"Killing process with pid {pid}")
                kill(pid,9)
        exit()