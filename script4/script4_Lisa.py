# Exercise: Thema 1, Script 4
# Author: Lisa Hu

# initialising variable
sequence = ''
codons = ''
protein = ''
header = ''
codonlength = 3
allowed_nucleic_symbols = "ACGTUIRYKMSWBDHVN-"
dna_codons = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
              'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
              'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
              'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
              'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
              'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
              'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
              'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
              'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
              'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
              'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
              'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
              'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
              'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
              'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
              'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
bye = True

# start code
new_file = open(input("What is the output file's name? "), 'w')     # opens output file of own input
sen_length = int(input('Enter line length: '))  # asks line length

# tries to open input and if it's not found, print error
try:
    files = open(input('Enter the file name: '))
except FileNotFoundError:
    print('No such file was found')

# while loop is true, main code
while bye:
    content = True
    # go through line of file
    for line in files:
        line = line.strip()     # remove newline
        if line.startswith('>'):
            header = line   # stores header
        # each lines goes into sequence and checks if the content is dna
        else:
            sequence += line.upper()    # stores sequence
            for character in line:
                if character not in allowed_nucleic_symbols:
                    content = False     # sets content False if not DNA
    # executes if file content True
    if content:
        for codon in range(0, len(sequence), codonlength):  # goes through sequence in triplets
            codons = sequence[codon:codon + codonlength]    # stores triplet in codon
            if len(codons) == 3:
                protein += dna_codons[codons]   # translates triplet to protein and stores
        print(header, file=new_file)    # prints header into the file

        for startposition in range(0, len(protein), sen_length):
            print(protein[startposition:startposition + sen_length], file=new_file)     # writes file in wanted format
        print(file=new_file)    # writes newline
        files.close()   # close input file

    if not content:     # error if file is not dna
        print("File contains wrong content")

    # asks for another file input
    question = input('Do you want to open another file? (y/n) ')
    if question == 'n':
        bye = False # breaks loop
    elif question == 'y':
        protein = ''    # clears variables for next file
        sequence = ''
        try:
            files = open(input('Enter the file name: '))    # looking for in in directory
        except FileNotFoundError:   # prints error if file not found
            print('No such file was found')
    else:   # if y/n input is false
        print('Incorrect input')

# close output file
new_file.close()

# end of code
