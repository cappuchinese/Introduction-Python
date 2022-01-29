# Exercise : Theme 1, script 6 (compulsory part only)
# Author   : Dave Langers (c) 2020


def process_sequence(header, sequence, mutation, outputfile, numchars=70):
    """"Function that mutates a sequence if required, and
    writes the header plus sequence to an open multi-FASTA file."""
    # Mutate the sequence if required
    if header[1:len(mutation[0])+1].upper() == mutation[0]:
        header += ' [ SEQUENCE ' + mutation[0] + ', MUTATED BY USER! ]'
        sequence = sequence[:mutation[1]-1] + mutation[3] + sequence[mutation[2]:]
    # If data is provided, write the header and sequence to file
    if header or sequence:
        print(header, file=outputfile)
        for position in range(0, len(sequence), numchars):
            print(sequence[position:position+numchars], file=outputfile)
        print(file=outputfile)   # Append an empty line


# Ask user for various inputs
print('Please enter on one line, separated by spaces:')
print('- the input filename;')
print('- the output filename;')
print('- the sequence identifier;')
print('- the start position of the mutation;')
print('- the end position of the mutation;')
print('- the mutation sequence;')
print('(e.g.: "original.fasta mutated.fasta NG_123456.7 10 15 ACT")')
inputname, outputname, identifier, start_pos, end_pos, insertion = input('? ').split()
if insertion == '-':
    insertion = ''
mutation = (identifier.upper(), int(start_pos), int(end_pos), insertion)

# Open input and output files
inputfile = open(inputname, 'r')
outputfile = open(outputname, 'w')

# Initialise empty header and sequence variables
header = ''
sequence = ''

# Loop through file to fill header and sequence variables
for line in inputfile:
    line = line.rstrip()   # Remove newline character
    if line.startswith('>'):
        process_sequence(header, sequence, mutation, outputfile)   # Write the previous sequence before starting a new one
        header = line
        sequence = ''
    else:
        sequence += line.upper()
process_sequence(header, sequence, mutation, outputfile)   # Don't forget the last sequence

# Close input and output files
inputfile.close()
outputfile.close()
