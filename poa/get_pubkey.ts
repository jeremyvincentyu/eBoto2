//Import Web3 Dependencies
import {Web3, Contract, ContractAbi, Web3BaseWallet, Web3BaseWalletAccount } from 'web3'

//Import ABI and address
import abi from "./abi.json"
import deployed_addresses from "./deployed_addresses.json"


async function main(){ 
const contract_address = deployed_addresses["eBoto#EA_Account"]

//Instantiate the Web3 Object and the Contract
const web3_instance = new Web3("http://127.0.0.1:8545")
const contract_instance = new web3_instance.eth.Contract(abi,contract_address)

//Call the address getter and log to stdout
const contract_authority_address: string = await contract_instance.methods.get_authority_address().call()
console.log(`Authority Address: ${contract_authority_address}`)

//Call the pubkey getter and log to stdout
const authority_pubkey: string = await contract_instance.methods.getAuthorityPubkey().call()
console.log(`Authority Pubkey: ${authority_pubkey}`)
process.exit()
}

main()