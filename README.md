I recommend that you download the eBoto 2.0 development VM instead of installing eBoto 2.0 and its dependencies directly on your machine. This development VM is a Virtualbox Appliance. The username of the VM is jeremy and its password is Riemann_9. This whole source tree is present in the VM in the directory /home/jeremy/Documents/eBoto2, with the installation process already done.  

However, if you insist on developing locally or want to set up your own containerization, here's what you have to do:  
1. Install these dependencies: npm, python3-venv, nginx, rsync. You can use your Linux distro's package manager to do this. For npm, you may prefer to install the latest npm directly from the NPM website.

2. Run bash install.sh, saying yes whenever prompted. You will need to provide your sudo password when prompted so that the nginx file gets copied to the correct place.  


To start eBoto 2.0, do the following(make sure to follow the steps in the correct order):
1. Run python3 reset.py
2. Run bash hardhat.sh in that same window and wait until the terminal says that the smart contract has been deployed
3. In another terminal window, run bash isolator.sh
4. In another terminal window, run bash authority.sh
5. Navigate to 127.0.0.1 in the browser.  

For some reason, attempting to combine steps 2 to 4 in start_instance.py using Python's subprocess module results in voters not being able to login during testing, among other unexplained bugs, but doing them separately results in a perfectly fine working setup.

The election authority's private key is in authority_daemon/data/authority.json.  

DO NOT use the authority.json here as the Election Authority's private key in an actual production system. This private key is only for development and testing, because it is public knowledge.  

Instead, generate a new Ethereum private key, replace authority.json with another authority.json containing that new private key in the same format, and edit eboto_hardhat/ignition/modules/deploy.ts, replacing authority_address and authority_pubkey with the Ethereum address and Ethereum public key corresponding to your new private key.  

Also, for production, replace the private keys in authority_daemon/data/initial_accounts.json with new private keys, since those private keys are already public knowledge by being in this public repository. 