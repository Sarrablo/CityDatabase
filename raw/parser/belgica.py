f = open("raw_bg.csv","a")
i = open("base_bg.txt")
ful = i.read()
i.close()

pais = "Belgium"
regiones = {}
provincias_name = {}
provincias_region = {}
departamento_provincia = {}

full = ful.split("\n")
for line in full:
    region = ""
    provincia = ""
    
    foo = line.split('|')
    if foo[0] == '1':
        regiones[foo[1]] = foo[4]
    elif foo[0] == '2':
        provincias_name[foo[1]] = foo[4]
        provincias_region[foo[1]] = foo[2]
    elif foo[0] == '3':
        departamento_provincia[foo[1]] = foo[2]
    elif foo[0] =='4':
        provincia = provincias_name[departamento_provincia[foo[2]]]
        region = regiones[provincias_region[departamento_provincia[foo[2]]]]
        f.write("%s;%s;%s;%s\n"%(pais, region, provincia, foo[4]))

f.close()
