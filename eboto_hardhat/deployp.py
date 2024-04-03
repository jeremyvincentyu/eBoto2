import subprocess
from time import sleep
#Start the Hardhat Node
start_node_command = "npx hardhat node"
node_instance = subprocess.Popen(start_node_command.split())
print("Blockchain Started")

sleep(10)



node_instance.wait()
