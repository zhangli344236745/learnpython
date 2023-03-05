from enum import IntEnum
from typing import Tuple,List

Nucleotide:IntEnum = IntEnum('Nucleotide',('A','C','G','T'))
Condon = Tuple[Nucleotide,Nucleotide,Nucleotide]
Gene = List[Condon]

gene_str: str = "ACGTGGCTCTTAACGTACGTACGTACGGGGTTTATATATACCCTACCCTAGGACTCCCCTTTT"
print(len(gene_str))

def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0,len(s),3):
        if (i+2) >= len(s):
            return gene
        condon: Condon = (Nucleotide[s[i]],Nucleotide[s[i+1]],Nucleotide[s[i+2]])
        gene.append(condon)
    return gene

my_gene: Gene = string_to_gene(gene_str)
print(my_gene)

def linnar_contains(gene:Gene,key_condon:Condon) -> bool:
    for condon in gene:
        if condon == key_condon:
            return True
    return False

acg: Condon = (Nucleotide.A,Nucleotide.C,Nucleotide.G)
gat: Condon = (Nucleotide.G,Nucleotide.A,Nucleotide.T)

print(linnar_contains(my_gene,acg))
print(linnar_contains(my_gene,gat))

def binary_contains(gene:Gene, key_condon: Condon) -> bool:
    low: int = 0
    hight: int = len(gene) - 1
    while low <= hight:
        mid = (low + hight) // 2
        if gene[mid] < key_condon:
            low = mid + 1
        elif gene[mid] > key_condon:
            hight = mid - 1
        else:
            return True
    return False

my_sorted_gene: Gene = sorted(my_gene)
print(binary_contains(my_sorted_gene,acg))
print(binary_contains(my_sorted_gene,gat))