f = open("raw_it.csv","a")
i = open("base_it.txt")
ful = i.read()
i.close()

pais = "Italy"
canton_actual = ""
distrito_actual = ""

full = ful.split("\n")
for line in full:
    foo = line.split('\t')
    if foo[2].startswith('-'):
        prov = foo[3]
    else:
        prov = foo[2]
    f.write("%s;%s;%s;%s\n"%(pais, foo[1], prov.strip(), foo[0].strip()))
    #print "%s;%s;%s;%s"%(pais, foo[1], prov.strip(), foo[0].strip())

f.close()
    
        
