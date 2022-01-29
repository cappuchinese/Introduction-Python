# script_02
# author Mats slik 2020


file_01 = open('ccr5_pro.fasta')
file_02 = open('ccr5_gen.fasta')
default_dict = {}
nucleotide_dict = {}
protein_dict = {}
dict_dict = {}
protein_m = 'M'
check_list = ['A', 'T', 'C', 'G']
counter_nuc = 0
counter_pro = 0
a = True
b = True
file_list = [file_01, file_02]
cg_percentage = 0

for line in file_01:
    line = line.strip()
    # print(line)
    if not line.startswith('>'):
        for let in line:
            if let in nucleotide_dict:
                nucleotide_dict[let] += 1
            else:
                nucleotide_dict[let] = 1
        if protein_m in nucleotide_dict:
            a = True
        else:
            a = False
file_01.close()

for line in file_02:
    line = line.strip()
    # print(line)
    if not line.startswith('>'):
        for let in line:
            if let in protein_dict:
                protein_dict[let] += 1
            else:
                protein_dict[let] = 1
        if protein_m in protein_dict:
            b = True
        else:
            b = False
file_02.close()

if a is True:
    G = nucleotide_dict['G']
    C = nucleotide_dict['C']
    A = nucleotide_dict['A']
    T = nucleotide_dict['T']
    cg_percentage = (G + C)/(G + C + A + T)*100
if a is False:
    print('File 01 contains nucleotide')
else:
    print('File 01 contains protein code')

if b is False:
    print('File 02 contains nucleotide')
else:
    print('File 02 contains protein code')

print('CG content in nucleotide code', cg_percentage)


print(a)
print(default_dict)
print(protein_dict)
print(nucleotide_dict)
print(dict_dict)


