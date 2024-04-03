import {Card} from '@mui/material'
import {DataGrid, GridColDef} from '@mui/x-data-grid'


interface ElectionResult{
    id: number,
    full_name: string,
    role: string,
    votes: number
}

export default function ViewResultUI({electionResults}: {electionResults: ElectionResult[]}){
       const columns: GridColDef[] = [
        {field:'id',headerName: "#",width: 50},
        {field: "full_name", headerName: "Full Name",width: 200},
        {field: "role", headerName: "Role", width: 100},
        {field: "votes", headerName: "Votes",width: 200},
        ]

return(

<Card elevation={8} style = {{padding: "1em"}}>
        <DataGrid
        rows={electionResults}
        columns={columns}
        initialState={{
        pagination:{
        paginationModel: {page:0, pageSize: 5}
        }
        }}
        pageSizeOptions ={[5]}
        />
</Card>

)

}
