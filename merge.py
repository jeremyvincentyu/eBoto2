from os import system
with open("conflict.txt","r") as conflict_file:
    conflict_lines = conflict_file.read().split("\n")
    for every_line in conflict_lines:
        line_fields = every_line.split()
        if len(line_fields)>1:
            conflict = line_fields[-1]
            system(f"git rm {conflict}")