cd eboto_hardhat

#Set the Authority Daemon's key to the hardhat key
cp /home/jeremy/Documents/new_eboto/authority_daemon/data/hardhat.json authority.json

python3 deploy.py deploy.ts