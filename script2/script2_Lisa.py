# Opdracht: Thema 1, Script 2
# Auteur: Lisa Hu

#opening files
open_np = open("ccr5_np.fasta")
open_nc = open("ccr5_nc.fasta")

#defining variables
dict_n = {}
lst_dict = []
files = [open_np, open_nc]
protein_m = "M"
DNA = True

#dna check function
def DNA_check(letter):
    nucleotides = ["A", "T", "C", "G"]
    if letter not in nucleotides:
        return False
    return True

#gc content function
def CG_perc(dict_n):
    return (dict_n["C"] + dict_n["G"]) / sum(dict_n.values())*100

#for loop opens both list of files, adding unknown letters to dict, checks if it's dna
for file in files:
    for line in file:
        line = line.strip()
        if not line.startswith(">"):
            for letter in line:
                if letter in dict_n:
                    dict_n[letter] += 1
                else:
                    dict_n[letter] = 1
                if DNA:
                    DNA = DNA_check(letter)
                    if DNA is True:
                        CG_perc(dict_n)
    lst_dict.append(dict_n)
    dict_n = {}
    print(file)
    print("DNA is", DNA_check(letter))

#printing information
print(lst_dict[0])
print(lst_dict[1])
print("CG content is :", CG_perc(lst_dict[1]), "%")