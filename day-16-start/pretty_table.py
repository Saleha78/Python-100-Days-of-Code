from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","squrtle","Charmander"])
table.add_column("Area", ["Electric", "water", "fire"])
table.align = "l"
print(table)