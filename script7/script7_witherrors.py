# Exercise : Theme 1, script 7 (compulsory part only)
# Author   : Dave Langers (c) 2020
# Note     : This file contains errors!


def read_genbank(inputname):
    """Function that reads all sections from a GenBank-file"""
    # Initialise variables
    section = ''   # Keeps track of the section we're working on
    sections = {}   # Keeps track of the contents of all sections
    # Open input file for reading
    inputfile = open(inputname)
    # Loop through the lines of the file
    for line in inputfile:
        # First, determine the section and content of this line
        if not line.startswith(' '):
            # This line is the start of a new section
            section = line[:12].rstrip()   # The first 12 characters contain the section identifier
            content = line[12:].strip()   # The other characters contain section content
        else:
            # This line is a continuation of an ongoing section...
            content = line.strip()   # All characters are considered continuing section content
        # Next, add the content to the section's dictionary value
        if section not in sections:
            # This is a new section, therefore create content
            sections[section] = content
        else:
            # This section already exists, therefore append content
            sections[section] += '\n'+content
    # Clean up
    inputfile.close()
    print('Finished reading file ...')
    return sections


def write_fasta(outputname, header, sequence, chars_per_line = 70):
    """Function that writes a FASTA-file's header and sequence"""
    # Open output file for writing
    outputfile = open("cf.fasta", "w")
    # Write header and sequence to output file
    print(header, file = outputfile)
    for position in range(0, len(sequence), chars_per_line):
        print(sequence[position: position+chars_per_line], file=outputfile)
    # Clean up
    outputfile.close()
    print('Finished writing file ...')


# Get filenames from user
print('Please enter your input file:')
inputname = input('? ')
print()

# Read GenBank file contents
genbank = read_genbank(inputname)
# Extract header in a single line
header = ">" + genbank["VERSION"]+' '+genbank["DEFINITION"]
header = header.replace('\n', ' ')
# Extract sequence without forbidden characters
sequence = genbank["ORIGIN"].upper()
for remove_char in ' 0123456789\n':
    sequence = sequence.replace(remove_char, '')
# Generate FASTA filename
extension = inputname.rindex('.')
outputname = inputname[: extension]+'.fasta'
# Write FASTA file contents
write_fasta(outputname, header, sequence)

# Report results to the screen
print('Sequence in', inputname, 'was successfully extracted to', outputname)
