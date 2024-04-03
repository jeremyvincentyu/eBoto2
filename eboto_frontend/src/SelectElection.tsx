import {Button} from "@mui/material"
import {DataGrid, GridColDef} from '@mui/x-data-grid'
import {MutableRefObject} from 'react'

function modify_election(){
    window.location.href = "#/modify_election"
}

interface Election{
    id: number,
    election_name: string,
    election_over : boolean,
    selected_election: MutableRefObject<string>,
    end_election: () => void
    view_election: ()=> void
}
interface ElectionRow{
    row: Election
}


function ElectionName(props: ElectionRow){
    //props.value is the value of the field in the row
    props.row.selected_election.current = props.row.election_name
    if (props.row.election_over){
        return (
        <Button variant="contained" onClick={props.row.view_election}> {props.row.election_name} </Button>
            )}
    else{
    return (
        <Button variant="contained" onClick={modify_election}> {props.row.election_name} </Button>
    )
    }
}

function EndButton(props: ElectionRow){
    props.row.selected_election.current = props.row.election_name
    if (props.row.election_over){
        return <></>
    }
    else{
    return (
        <Button variant="contained" onClick={props.row.end_election}> End Election </Button>
    )
    }
}


interface SelectElectionInterface{
    election_list: Election[]
}


export default function SelectElectionUI({election_list}: SelectElectionInterface){
    const columns: GridColDef[] = [
    {field:'id',headerName: "#",width: 30},
    {field: "election_name", headerName: "Election Name", width: 250, renderCell: ElectionName},
    {field: "status", headerName: "Status", width: 150},
    {field:"end", headerName:"End", width: 150, renderCell: EndButton}
    ]


    return(
    <DataGrid
    columns={columns}
    rows={election_list}
    initialState={{
        pagination:{
        paginationModel: {page:0, pageSize: 50}
        }
        }}
    pageSizeOptions ={[50]}
    />
    )
}
