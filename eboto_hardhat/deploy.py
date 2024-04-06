from sys import argv
import subprocess
from time import sleep

#Start the Hardhat Node
start_node_command = "npx hardhat node"
node_instance = subprocess.Popen(start_node_command.split())
print("Blockchain Started")

sleep(10)

#Erase the old history
erase_history_command = "rm -rf ignition/deployments/chain-31337"
subprocess.run(erase_history_command.split())


#Deploy the contract
deploy_contract_command = f"npx hardhat ignition deploy ignition/modules/{argv[1]} --network localhost"
subprocess.run(deploy_contract_command.split())

print("Contract Deployed")

#Generate the abis
abi_command = "npx solc@0.8.19 --abi contracts/EA_Account.sol"
subprocess.run(abi_command.split())




node_instance.wait()
