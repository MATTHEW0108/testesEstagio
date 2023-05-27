

file = "//data/Relatorio_cadopVue.csv"

def busca (file, info):
    with open (file, 'r'):
        for line in file:
            line = line.strip("\n")
            if info in line:
                print(line)
            