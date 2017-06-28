f = open("raw_ad.csv","a")
i = open("base_ad.txt")
ful = i.read()
i.close()

pais = "Andorra"
canton_actual = "All"
distrito_actual = ""

full = ful.split("\n")
for line in full:
    foo = line.split('.')
    f.write("%s;%s;%s;%s\n"%(pais, canton_actual, foo[1].strip(),foo[0].strip()))

f.close()
    
        
