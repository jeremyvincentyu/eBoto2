from os import system

with open("ephemeral.txt","r") as ephemeral_file:
    ephemeral_lines = ephemeral_file.read().split("\n")
    for every_line in ephemeral_lines:
        ephemeral_list = every_line.split()
        if len(ephemeral_list)>0:
            system(f"rm {ephemeral_list[0]}")