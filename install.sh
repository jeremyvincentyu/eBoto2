python3 -m venv authority_darmon
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