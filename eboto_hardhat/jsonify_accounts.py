import json
json_output: list[dict[str,str]] =[]

with open("accounts.txt","r") as non_json_file:
    current_address: str = ""
    current_key:str = ""
    for every_line in non_json_file:
        digested_line = every_line.split()
        
        #If the word "Account" is in the line, recover the address
        if "Account" in every_line:
            current_address = digested_line[2]
        
        #If the word "Private"is in the line, recover the private key
        if "Private" in every_line:
            current_key = digested_line[2].strip()
            packaged = {"private": current_key,"address": current_address}
            json_output.append(packaged)

with open("initial_accounts.json","w") as json_file:
    json_file.write(json.dumps(json_output))