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

# Output line length
chars_per_line = 70

# Open files
inputfile = open(input('Nucleotide file for input ? '), 'r')
outputfile = open(input('Aminoacid file for output ? '), 'w')

# Initialise some variables
nucleo_buffer = ''
amino_buffer = ''
# Loop through file and write output while reading input
for line in inputfile:
    line = line.rstrip()   # Remove newline character
    if line.startswith('>'):
        # The header is written unchanged
        print(line, file=outputfile)
    else:
        # The nucleotide sequence is translated to aminoacids
        nucleo_buffer += line.upper()
        while len(nucleo_buffer) >= 3:
            # Translate triplet to aminoacid
            amino_buffer += codons[nucleo_buffer[:3]]
            nucleo_buffer = nucleo_buffer[3:]
            # Output the result
            if len(amino_buffer) == chars_per_line:
                print(amino_buffer, file=outputfile)
                amino_buffer = ''
# Don't forget remaining aminoacids
print(amino_buffer, file=outputfile)

# Close files
inputfile.close()
outputfile.close()

# Feedback to the user on-screen
print('Translation successfully completed!')
