f = open("raw_nh.csv","a")
i = open("base_nh.txt")
ful = i.read()
i.close()

pais = "Netherlands"
canton_actual = "All"
distrito_actual = ""

full = ful.split("\n")
for line in full:
    foo = line.split("\t")
    if foo[1].startswith("Province"):
        distrito_actual = foo[0]
    elif foo[1].startswith("Municipality"):
        csv = ("%s;%s;%s;%s"%(pais,canton_actual,distrito_actual,foo[0]))
        f.write("%s\n"%(csv))
        
f.close()
