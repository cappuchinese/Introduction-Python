# script_05
# author Mats Slik 2020

input_file = input('type here your import file name: ')
export_file_input = input('type here your export file name: ')
export_file = open(export_file_input, 'w')
sequence_mrna = ''
header_mrna = ''
count = 0
Codon_length = 3
codon = ''
amino_string = ''
codon_dict_freq = {}
invers_codon_dict = {'I': ['ATA', 'ATC', 'ATT'],
                     'M': ['ATG'],
                     'F': ['TTT', 'TTC'],
                     'L': ['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'],
                     'V': ['GTT', 'GTC', 'GTA', 'GTA'],
                     'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
                     'P': ['CCT', 'CCC', 'CCA', 'CCG'],
                     'T': ['ACT', 'ACC', 'ACA', 'ACG'],
                     'A': ['GCT', 'GCC', 'GCA', 'GCG'],
                     'Y': ['TAT', 'TAC'],
                     '_': ['TAA', 'TAG', 'TGA'],
                     'H': ['CAT', 'CAC'],
                     'Q': ['CAA', 'CAG'],
                     'N': ['AAT', 'AAC'],
                     'K': ['AAA', 'AAG'],
                     'D': ['GAT', 'GAC'],
                     'E': ['GAA', 'GAG'],
                     'C': ['TGT', 'TGC'],
                     'W': ['TGG'],
                     'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
                     'G': ['GGT', 'GGC', 'GGA', 'GGG']
                     }
codon_dict = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
}
result_dict = {}
open_input_file = open(input_file, 'r')

for line in open_input_file:
    line_striped = line.strip()
    if line_striped.startswith('>'):
        header_mrna = line_striped
    elif line_striped:
        sequence_mrna += line_striped.upper()

for char in sequence_mrna:
    if count < Codon_length:
        codon += char
        count += 1
    elif count == Codon_length:
        amino_string += codon_dict[codon]
        if codon not in codon_dict_freq:
            codon_dict_freq[codon] = 1
        else:
            codon_dict_freq[codon] += 1

        codon = ''
        count = 0

# determining of most frequent used codon coding for a amino acid
for key in invers_codon_dict.keys():
    num = 0
    for triplet in invers_codon_dict[key]:
        if triplet not in codon_dict_freq:
            pass
        else:
            codon_freq = codon_dict_freq[triplet]
            codon_freq = int(codon_freq)
            if codon_freq > num:
                num = codon_freq
                result_dict[key] = triplet





print(amino_string)
print()
print(codon_dict_freq)
print()
print(invers_codon_dict)
print()
print(result_dict)
