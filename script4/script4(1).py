# Exercise : Theme 1, script 4 (compulsory part only)
# Author   : Dave Langers (c) 2020


# Codon-table
codons = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
    'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}

# Get filenames from user
print('Please enter your input file with nucleotides:')
inputname = input('? ')
print('Please enter your output file with aminoacids:')
outputname = input('? ')
print()

# Open input file
inputfile = open(inputname, 'r')
# Initialise empty header and sequence variables
header = ''
sequence = ''
# Loop through file to fill header and sequence variables
for line in inputfile:
    line = line.rstrip()   # Remove newline character
    if line.startswith('>'):
        header = line   # Remember header
    else:
        sequence += line.upper()   # Add capitalised sequence
# Close the input file
inputfile.close()

# Translate triplets to aminoacids
aminoacids = ''
for position in range(0, len(sequence) - 2, 3):   # Minus two to skip last incomplete triplet
    triplet = sequence[position:position + 3]
    aminoacids += codons[triplet]

# Open output file for writing
outputfile = open(outputname, 'w')
# Write header and sequence to output file
print(header, file = outputfile)
for position in range(0, len(aminoacids), 70):
    print(aminoacids[position:position + 70], file=outputfile)
# Close output file for writing
outputfile.close()

# Report results to the screen
print('Sequence in', inputname, 'was successfully translated to', outputname)
