import subprocess
from time import sleep
from os import kill
#Start the hardhat first,
hardhat_process = subprocess.Popen("bash hardhat.sh".split(),stdout=subprocess.PIPE, stdin = subprocess.PIPE, stderr=subprocess.PIPE)
sleep(10)
 
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
            if "flask" in every_line:
                line_contents = every_line.split()
                pid = int(line_contents[1])
                print(f"Killing process with pid {pid}")
                kill(pid,9)
        exit()