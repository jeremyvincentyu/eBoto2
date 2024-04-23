cd poa
source bin/activate
bash src/deploy.sh
cd ..
python3 poa/src/deploy.py
cd eboto_frontend
bash publish.sh
