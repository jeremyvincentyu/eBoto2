from web3 import Web3

def get_nonce(some_address: str)->str:
    web3_instance = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    return str(web3_instance.eth.get_transaction_count(Web3.to_checksum_address(some_address)))