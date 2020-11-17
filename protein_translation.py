# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 19:09:18 2020

@author: TONG
"""

#!/usr/bin/python3
#Generate amino acid sequence which is translated from DNA sequence in ".txt" file and perform residues statistics
str = "Generator of amino acids sequence"
print (str.center(80, '*'),'\n')
str = "Designed by Dr.Tong Li, School of Medicine, Tsinghua University, Beijing, China"
print (str.center(80, ' '),'\n')

with open(input("Please specify your DNA .txt file:"),'r',encoding='utf-8') as f:
  sequence = f.read()
  
seq_len = sequence = sequence.upper()

sequence = ' '.join([sequence[i:i+3] for i in range(0, len(sequence), 3)]) #adding space in every three bases

str = "Original DNA sequence is"
print (str.center(80, '*'),'\n')

print(sequence,'\n')

print("The DNA length is:",len(seq_len),"bp")
a='A'; t='T'; c='C'; g='G'
print ("Number of 'A' base: ", sequence.count(a))
print ("Number of 'T' base: ", sequence.count(t))
print ("Number of 'C' base: ", sequence.count(c))
print ("Number of 'G' base: ", sequence.count(g))
print ("Number of 'A+T' bases: ", sequence.count(a)+sequence.count(t))
print ("Number of 'C+G' bases: ", sequence.count(c)+sequence.count(g))
print ("CG content: ", round((sequence.count(c)+sequence.count(g))/len(sequence)*100,2),'%') 
print ("AT content: ", round((sequence.count(a)+sequence.count(t))/len(sequence)*100,2),'%') 
print('\n')

#define the condon dictionary
codon_dict = {
        "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", 
        "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
        "UAU":"Y", "UAC":"Y", "UAA":".", "UAG":".",
        "UGU":"C", "UGC":"C", "UGA":".", "UGG":"W",
        "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
        "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
        "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
        "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
        "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
        "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
        "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
        "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
        "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
        "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
        "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
        "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",
        } 

#mRNA sequence
sequence = sequence.replace("T", "U") 


t = [] #define a void list for storage of amino acids
for i in range(0, len(sequence), 4):
    t.append(codon_dict[(sequence[i:i+3])])
    
protein = ''.join(t) #transform list t to string 

str = "Amino acid sequence is"
print (str.center(80, '*'),'\n')
print(protein,'\n')

print("This protein has", len(protein)-1, "residues")
print ("Ala (A):", protein.count("A"),' ', round(protein.count("A")/(len(protein)-1)*100,2),'%')
print ("Arg (R):", protein.count("R"),' ', round(protein.count("R")/(len(protein)-1)*100,2),'%')
print ("Asn (N):", protein.count("N"),' ', round(protein.count("N")/(len(protein)-1)*100,2),'%')
print ("Asp (D):", protein.count("D"),' ', round(protein.count("D")/(len(protein)-1)*100,2),'%')
print ("Cys (C):", protein.count("C"),' ', round(protein.count("C")/(len(protein)-1)*100,2),'%')
print ("Gln (Q):", protein.count("Q"),' ', round(protein.count("Q")/(len(protein)-1)*100,2),'%')
print ("Glu (E):", protein.count("E"),' ', round(protein.count("E")/(len(protein)-1)*100,2),'%')
print ("Gly (G):", protein.count("G"),' ', round(protein.count("G")/(len(protein)-1)*100,2),'%')
print ("His (H):", protein.count("H"),' ', round(protein.count("H")/(len(protein)-1)*100,2),'%')
print ("Ile (I):", protein.count("I"),' ', round(protein.count("I")/(len(protein)-1)*100,2),'%')
print ("Leu (L):", protein.count("L"),' ', round(protein.count("L")/(len(protein)-1)*100,2),'%')
print ("Lys (K):", protein.count("K"),' ', round(protein.count("K")/(len(protein)-1)*100,2),'%')
print ("Met (M):", protein.count("M"),' ', round(protein.count("M")/(len(protein)-1)*100,2),'%')
print ("Phe (F):", protein.count("F"),' ', round(protein.count("F")/(len(protein)-1)*100,2),'%')
print ("Pro (P):", protein.count("P"),' ', round(protein.count("P")/(len(protein)-1)*100,2),'%')
print ("Ser (S):", protein.count("S"),' ', round(protein.count("S")/(len(protein)-1)*100,2),'%')
print ("Thr (T):", protein.count("T"),' ', round(protein.count("T")/(len(protein)-1)*100,2),'%')
print ("Trp (W):", protein.count("W"),' ', round(protein.count("W")/(len(protein)-1)*100,2),'%')
print ("Tyr (Y):", protein.count("Y"),' ', round(protein.count("Y")/(len(protein)-1)*100,2),'%')
print ("Val (V):", protein.count("V"),' ', round(protein.count("V")/(len(protein)-1)*100,2),'%','\n')
print("total number of negatively charged residues:", protein.count("D")+protein.count("E"),' ', round(((protein.count("D")+protein.count("E")))/(len(protein)-1)*100,2),'%')
print("total number of positively charged residues:", protein.count("R")+protein.count("K"),' ', round(((protein.count("K")+protein.count("R")))/(len(protein)-1)*100,2),'%')



