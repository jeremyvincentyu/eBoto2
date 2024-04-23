from threading import Thread
from time import sleep
import subprocess

password = input("Enter the same password you entered when resetting")
#Clef in background
def run_clef():
    subprocess.run("bash clef_helper.sh".split(),text=True,input=password)

#Start Clef
clef_thread = Thread(target=run_clef)
clef_thread.start()
sleep(5)


#Start Geth
subprocess.run("bash geth_helper.sh".split())