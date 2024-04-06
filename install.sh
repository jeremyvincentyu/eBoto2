mkdir isolator/data/elections
mkdir authority_daemon/data/control_keys
mkdir authority_daemon/data/dates
mkdir authority_daemon/data/roles
sudo cp default /etc/nginx/sites-enabled
sudo systemctl restart nginx
python3 -m venv authority_daemon
python3 -m venv isolator
cd authority_daemon
npm install
source bin/activate
pip install -r requirements.txt
deactivate
cd ..
cd isolator
npm install
source bin/activate
pip install -r requirements.txt
deactivate
cd ..
cd eboto_frontend
npm install
bash publish.sh
cd ..
cd eboto_hardhat
npm install