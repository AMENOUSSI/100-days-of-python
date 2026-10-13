from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Matieres",["Maths","Ang","HG"])
table.add_column("Type",["Maths","Ang","HG"])

table.align = "l"

print(table)