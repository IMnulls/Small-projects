def proteinsequence (rna):
    print(type(rna))
    print(rna)
    stopseq={"UAA", "UAG", "UGA"}
    if all(x in ('A', 'U', 'G', 'C') for x in rna) == False:
        rna=str(input("Input incorrect. Make sure that the input contains only A, U, G and C."))
        return proteinsequence(rna)
    try:
        rna=rna[(rna.index("AUG")):]
        rna = [rna[i:i+3] for i in range(0, len(rna), 3)]
    except:
        rna=str(input("Missing start codon. Make sure the input contains a start codon"))
        return proteinsequence(rna)
    try:
        rna = rna[:[i for i, val in enumerate(rna) if val in stopseq][0]+1]
    except:
        rna=str(input("Missing stop codon. Make sure the input contains a stop codon"))
        return proteinsequence(rna)
        

    protein=["Start", "Stop"]
    
    for i in range (len(rna)):
        if rna[i] in {"UUU", "UUC"}:
            protein.insert(-1, "Phe")
            
        elif rna[i] in {"UUA", "UUG", "CUU", "CUC", "CUA", "CUG"}:
            protein.insert(-1, "Leu")

        elif rna[i] in {"AUU", "AUC", "AUA"}:
            protein.insert(-1, "Ile")

        elif rna[i] in {"GUU", "GUC", "GUA", "GUG"}:
            protein.insert(-1, "Val")

        elif rna[i] in {"UCU", "UCC", "UCA", "UCG", "UGU", "UGC"}:
            protein.insert(-1, "Ser")

        elif rna[i] in {"CCU", "CCC", "CCA", "CCG"}:
            protein.insert(-1, "Pro")
  
        elif rna[i] in {"ACU", "ACC", "ACA", "ACG"}:
            protein.insert(-1, "Thr")

        elif rna[i] in {"GCU", "GCC", "GCA", "GCG"}:
            protein.insert(-1, "Ala")

        elif rna[i] in {"UAU", "UAC"}:
            protein.insert(-1, "Tyr")
       
        elif rna[i] in {"CAU", "CAC"}:
            protein.insert(-1, "His")
          
        elif rna[i] in {"CAA", "CAG"}:
            protein.insert(-1, "Gln")
  
        elif rna[i] in {"AAU", "AAC"}:
            protein.insert(-1, "Asn")
    
        elif rna[i] in {"AAA", "AAG"}:
            protein.insert(-1, "Lys")
    
        elif rna[i] in {"GAU", "GAC"}:
            protein.insert(-1, "Asp")
    
        elif rna[i] in {"GAA", "GAG"}:
            protein.insert(-1, "Glu")
      
        elif rna[i] in {"UGU", "UGC"}:
            protein.insert(-1, "Cys")
         
        elif rna[i] in {"UGG"}:
            protein.insert(-1, "Trp")
      
        elif rna[i] in {"CGU", "CGC", "CGA", "CGG", "AGA", "AGG"}:
            protein.insert(-1, "Arg")
     
        elif rna[i] in {"GGU", "GGC", "GGA", "GGG"}:
            protein.insert(-1, "Gly")
            
    return(protein)
