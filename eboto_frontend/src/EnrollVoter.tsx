import {TextField, Grid, Button, Card,Typography} from "@mui/material"
import {DataGrid, GridColDef} from '@mui/x-data-grid'
import {useState, MutableRefObject} from 'react'
import EthCrypto  from 'eth-crypto';
import {Web3, Contract, ContractAbi, Web3BaseWallet, Web3BaseWalletAccount} from 'web3'

interface VoterRow{
    id: number,
    eth_address: string,
    pubkey: string,
    full_name: string
    elections_joined: string[]
}

interface PackedWallet{
    web3: Web3,
    contract: Contract<ContractAbi>,
    account: Web3BaseWallet<Web3BaseWalletAccount>
}

function VotersCard({rows}: {rows: VoterRow[]}){
    const columns: GridColDef[] = [
        {field:'id',headerName: "#",width: 30},
        {field: "eth_address", headerName: "Ethereum Address",width: 160},
        {field: "pubkey",headerName: "Public Key", width: 160},
        {field: "full_name", headerName: "Full Name",width: 160},
    ]




    return (
        <Card elevation = {8} style = {{padding: "1em"}}>
        <Grid container>

        <Grid item xs={12}>
        <DataGrid
        rows={rows}
        columns={columns}
        initialState={{
        pagination:{
        paginationModel: {page:0, pageSize: 20}
        }
        }}
        pageSizeOptions ={[20]}
        />
        </Grid>


        <Grid item xs={12}>
        <Typography component = "h5" variant="h5">
        Voter Accounts in Database
        </Typography>
        </Grid>

        </Grid>
        </Card>
    )
}

async function enrollVoter(ethereum_wallet: MutableRefObject<PackedWallet>, full_name: string, address: string ,pubkey: string){
   const salt_array= new Uint32Array(5)
   const plain_name_object = {actual_name: full_name, salt:crypto.getRandomValues(salt_array)}
   const salted_name_string = JSON.stringify(plain_name_object)
   const private_key = ethereum_wallet.current.account[0].privateKey
   const public_key = EthCrypto.publicKeyByPrivateKey(private_key)
   const ea_address= ethereum_wallet.current.account[0].address
   const encrypted_name_object = await EthCrypto.encryptWithPublicKey(public_key,salted_name_string)
   const encrypted_name_string = EthCrypto.cipher.stringify(encrypted_name_object)
   await ethereum_wallet.current.contract.methods.enrollVoter(encrypted_name_string,address,pubkey).send({from: ea_address})
}


interface NewCardInterface{
    setRows: (newRows: (oldRows: VoterRow[]) => VoterRow[]) => void,
    ethereum_wallet: MutableRefObject<PackedWallet>
}

function NewCard({setRows,ethereum_wallet}: NewCardInterface){
    const [newVoterAddress,setnewVoterAddress] = useState("")
    const [newVoterName, setnewVoterName] = useState("")
    const [newVoterPubkey, setnewVoterPubkey] = useState("")
    const addNewVoter = ()=>{

    enrollVoter(ethereum_wallet, newVoterName, newVoterAddress, newVoterPubkey).then(()=>{
    setRows((old_rows)=>[...old_rows,{id: old_rows.length, full_name: newVoterName, eth_address: newVoterAddress, pubkey: newVoterPubkey, elections_joined: []}])
    setnewVoterName("")
    setnewVoterAddress("")
    setnewVoterPubkey("")
    })
    }

    return (
    <Card elevation = {8} style = {{padding: "1em"}} >

    <Grid container rowSpacing={5}>

    <Grid item xs={12}>
    <TextField label="Ethereum Address" value={newVoterAddress} onChange={(e)=>setnewVoterAddress(e.target.value)}/>
    </Grid>

    <Grid item xs={12}>
    <TextField label="Voter Public Key" value={newVoterPubkey} onChange={(e)=>setnewVoterPubkey(e.target.value)}/>
    </Grid>

    <Grid item xs={12}>
    <TextField label="Name" value={newVoterName} onChange={(e)=>setnewVoterName(e.target.value)}/>
    </Grid>



    <Grid item xs={12}>
    <Button variant="contained" onClick={addNewVoter}> Enroll Voter </Button>
    </Grid>

    </Grid>

    </Card>
    )
}

interface EnrollVoterInterface{
    rows: VoterRow[],
    setRows: (newRows: (oldRows: VoterRow[]) => VoterRow[]) => void,
    ethereum_wallet: MutableRefObject<PackedWallet>
}

export default function EnrollVoterUI({rows,setRows,ethereum_wallet}: EnrollVoterInterface){

    return (
        <Grid container columnSpacing={20}>

        <Grid item xs= {6}>
        <VotersCard rows={rows}/>
        </Grid>

        <Grid item xs={6}>
        <NewCard setRows={setRows} ethereum_wallet={ethereum_wallet}/>
        </Grid>

        </Grid>
    )
}
