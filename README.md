I recommend that you download the eBoto 2.0 development VM instead of installing eBoto 2.0 and its dependencies directly on your machine. This development VM is a Virtualbox Appliance. The username of the VM is jeremy and its password is Riemann_9. This whole source tree is present in the VM in the directory /home/jeremy/Documents/eBoto2, with the installation process already done.  

However, if you insist on developing locally or want to set up your own containerization, here's what you have to do:  
1. Install these dependencies: npm, python3-venv, nginx, rsync. You can use your Linux distro's package manager to do this. For npm, you may prefer to install the latest npm directly from the NPM website.

2. Run bash install.sh, saying yes whenever prompted. You will need to provide your sudo password when prompted so that the nginx file gets copied to the correct place.  


To start eBoto 2.0, simply run python3 start_instance.py(after installing, or you can run this immediately if you're using the development VM), and navigate to 127.0.0.1 in the browser.  

The election authority's private key is in authority_daemon/data/authority.json.  

DO NOT use the authority.json here as the Election Authority's private key in an actual production system. This private key is only for development and testing, because it is public knowledge.  

Instead, generate a new Ethereum private key, replace authority.json with another authority.json containing that new private key in the same format, and edit eboto_hardhat/ignition/modules/deploy.ts, replacing authority_address and authority_pubkey with the Ethereum address and Ethereum public key corresponding to your new private key.  

Also, for production, replace the private keys in authority_daemon/data/initial_accounts.json with new private keys, since those private keys are already public knowledge by being in this public repository. 