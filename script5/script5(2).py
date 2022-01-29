# Exercise : Theme 1, script 5 (compulsory part only)
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


def read_fasta(inputname):
    """Function that reads a FASTA-file and returns the header and sequence as strings"""
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
    # Return results
    return header, sequence


def write_fasta(outputname, header, sequence, chars_per_line=70):
    """Function that writes a FASTA-file's header and sequence"""
    # Open output file for writing
    outputfile = open(outputname, 'w')
    # Write header and sequence to output file
    print(header, file=outputfile)
    for position in range(0, len(sequence), chars_per_line):
        print(sequence[position:position+chars_per_line], file = outputfile)
    # Close output file for writing
    outputfile.close()


# Ask user for various files
print('Please enter your nucleotide file(s) to count triplets from (separated by spaces):')
nucleo_filenames = input('? ').split()
print('Please enter your input aminoacid file:')
input_filename = input('? ')
print('Please enter your output nucleotide file:')
output_filename = input('? ')
print()

# Initialise triplet counter dictionary
counter = dict()
for codon in codons:
    counter[codon] = 0

# Loop through all nucleotide files
for nucleo_filename in nucleo_filenames:
    # Read file contents
    nucleo_header, nucleo_sequence = read_fasta(nucleo_filename)
    # Count triplets
    for position in range(0, len(nucleo_sequence)-2):   # Minus two to skip last incomplete triplet
        codon = nucleo_sequence[position:position+3]
        counter[codon] += 1

# Initialise the aminoacids reverse-translation table
aminoacids = dict()
for codon in codons:
    aminoacid = codons[codon]
    aminoacids[aminoacid] = ''
# Determine most common codon for each aminoacid
for aminoacid in aminoacids:
    best_count = -1   # Initialise to a worst possible count
    for codon in codons:
        if codons[codon] == aminoacid and counter[codon] > best_count:
            # Store new best codon in aminoacids reverse-translation table
            aminoacids[aminoacid] = codon
            best_count = counter[codon]

# Read the aminoacid file contents
amino_header, amino_sequence = read_fasta(input_filename)
# Convert aminoacid sequence to nucleotides
nucleo_sequence = ''
for aminoacid in amino_sequence:
    nucleo_sequence += aminoacids[aminoacid]
# Write the result to the nucleotide file
write_fasta(output_filename, amino_header, nucleo_sequence)

# Report results to the screen
print('Sequence in', input_filename, 'was successfully reverse-translated to', output_filename)
