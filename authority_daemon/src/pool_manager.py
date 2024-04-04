import json
account_pool: list[dict[str,str]] = []

with open("data/account_pool.json","r") as pool_file:
    account_pool = json.loads(pool_file.read())

def allocate_accounts(n: int, requesting_election: str)->list[dict[str,str]]:
    global account_pool
    assert(len(account_pool)>=n)
    allocated_accounts = account_pool[:n]
    remaining_accounts = account_pool[n+1:]
    account_pool = remaining_accounts
    
    with open("data/account_pool.json","w") as pool_file:
        pool_file.write(json.dumps(account_pool))
    
    with open(f"data/control_keys/{requesting_election}.json","w") as election_file:
        election_file.write(json.dumps(allocated_accounts))
    

    return allocated_accounts