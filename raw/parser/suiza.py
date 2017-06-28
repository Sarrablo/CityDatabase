f = open("raw_sw.csv","a")
i = open("base_sw.txt")
ful = i.read()
i.close()

pais = "Switzerland"
canton_actual = ""
distrito_actual = ""

full = ful.split("\n")
for line in full:
    if line.startswith("-"):
        canton_actual = line[2:]
    elif line.startswith(">>"):
        distrito_actual = line[3:]
    elif line.startswith("......"):
        csv = ("%s;%s;%s;%s"%(pais,canton_actual,distrito_actual,line[11:]))
        f.write("%s\n"%(csv))
        
