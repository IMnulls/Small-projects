def analyzedna(dna):
    a, c, g, t = 0, 0, 0, 0
    for i in range(len(dna)):
        if dna[i]=="A":
            a+=1
        elif dna[i]=="C":
            c+=1
        elif dna[i]=="G":
            g+=1
        elif dna[i]=="T":
            t+=1
        else:
            dna=str(input("Input incorrect. Please make sure the input contains only A, T, G and C."))
            analyzedna(dna)
    print (f"A:{a} C:{c} G:{g} T:{t}")
