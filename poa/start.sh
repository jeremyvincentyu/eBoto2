rm -rf data
geth init --datadir data genesis.json
geth --datadir data account new