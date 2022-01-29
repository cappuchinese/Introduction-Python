# Exercise : Theme 1, script 7 (compulsory part only)
# Author   : Dave Langers (c) 2018


def read_genbank(inputname):
    """Function that reads all sections from a GenBank-file"""
    section = ''
    sections = dict()
    # Loop through the lines of the file
    inputfile = open(inputname)
    for line in inputfile:
        if not line.startswith(' '):
            # This line is the start of a new section
            section = line[:12].rstrip()   # The first 12 characters contain the section identifier
            content = line[12:].strip()   # The other characters contain section content
        else:
            # This line is a continuation of an ongoing section...
            content = line.strip()   # All characters are considered continuing section content
        if section not in sections:
            # This is a new section, therefore create content
            sections[section] = content
        else:
            # This section already exists, therefore append content
            sections[section] += '\n'+content
    print(sections)
    inputfile.close()
    return sections


def write_fasta(outputname, header, sequence, chars_per_line = 70):
    """Function that writes a FASTA-file's header and sequence"""
    # Open output file for writing
    outputfile = open(outputname, 'w')
    # Write header and sequence to output file
    print(header, file = outputfile)
    for position in range(0, len(sequence), chars_per_line):
        print(sequence[position:position+chars_per_line], file = outputfile)
    # Close output file for writing
    outputfile.close()


# Get filenames from user
print('Please enter your input file:')
inputname = input('? ')
print()

# Read GenBank file contents
genbank = read_genbank(inputname)
# Extract header
header = '>'+genbank['VERSION']+' '+genbank['DEFINITION']
header = header.replace('\n', ' ')
# Extract sequence
sequence = genbank['ORIGIN'].upper()
for remove_char in ' 0123456789\n':
    sequence = sequence.replace(remove_char, '')
# Generate FASTA filename
extension = inputname.rindex('.')
outputname = inputname[:extension]+'.fasta'
# Write FASTA file contents
write_fasta(outputname, header, sequence)

# Report results to the screen
print('Sequence in', inputname, 'was successfully extracted to', outputname)
