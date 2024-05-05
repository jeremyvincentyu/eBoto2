cd testing
source bin/activate
export PYTHONPATH=$PYTHONPATH:src
python3 src/setup_election.py $1 $2
