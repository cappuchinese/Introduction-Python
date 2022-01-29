dict_np = {}
dict_nc = {}
lst_dict = []

open_np = open("ccr5_np.fasta")
open_nc = open("ccr5_nc.fasta")
files = [open_np, open_nc]
protein_m = "M"

DNA = True

def DNA_check(letter):
    nucleotides = ["A", "T", "C", "G"]
    if letter not in nucleotides:
        return False
    return True

def CG_perc(dict_np):
    return (dict_np["C"] + dict_np["G"]) / sum(dict_np.values())*100

for file in files:
    for line in file:
        line = line.strip()
        if not line.startswith(">"):
            for letter in line:
                if letter in dict_np:
                    dict_np[letter] += 1
                else:
                    dict_np[letter] = 1
                if DNA:
                    DNA = DNA_check(letter)
                    if DNA is True:
                        CG_perc(dict_np)
                        #dict_np["G"] = G
                        #dict_np["C"] = C
                        #dict_np["A"] = A
                        #dict_np["T"] = T
                        #GC_content = (G + C) / (A + C + T + G) * 100
    lst_dict.append(dict_np)
    dict_np = {}
    print(DNA_check(letter))
print(lst_dict[0])
print(lst_dict[1])



open_np.close()
open_nc.close()

# maybe def something