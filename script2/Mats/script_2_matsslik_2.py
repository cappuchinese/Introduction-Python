# script_02
# author Mats slik 2020

# opening of used files
file_01 = open('ccr5_gen.fasta')
file_02 = open('ccr5_pro.fasta')

# defining of  variabels
nucleotide_dict = {}
protein_dict = {}
protein_m = 'M'

a = True
b = True

cg_percentage = 0

# first for loop for file_01 opening.
# and detecting and handeling of functions
for line in file_01:
    line = line.strip()
    # print(line)
    if not line.startswith('>'):
        for let in line:
            # automatic adding
            if let in nucleotide_dict:
                nucleotide_dict[let] += 1
            else:
                nucleotide_dict[let] = 1
        if protein_m in nucleotide_dict:
            a = False
file_01.close()

# second for loop for file_02 opening.
# and detecting and  handeling of functions
for line in file_02:
    line = line.strip()
    # print(line)
    if not line.startswith('>'):
        for let in line:
            if let in protein_dict:
                protein_dict[let] += 1
            else:
                protein_dict[let] = 1
        if not protein_m in protein_dict:
            b = False
file_02.close()

# calculation of cg content if it is nucleotides for file_01
if a is True: #moet True zijn
    G = nucleotide_dict['G']
    C = nucleotide_dict['C']
    A = nucleotide_dict['A']
    T = nucleotide_dict['T']
    cg_percentage = (G + C)/(G + C + A + T)*100
    print('CG content in nucleotide code', cg_percentage)
if a is False:
    print('File 01 contains protein code')
print(nucleotide_dict)

# calculation of cg content if it is nucleotides for file_02
if b is False:
    G = nucleotide_dict['G']
    C = nucleotide_dict['C']
    A = nucleotide_dict['A']
    T = nucleotide_dict['T']
    cg_percentage = (G + C)/(G + C + A + T)*100
    print('CG content in nucleotide code', cg_percentage,'%') # print mooiere strings
    print('File 02 contains nucleotide')
else:
    print('File 02 contains protein code')
print(protein_dict)
