# Exercise : Theme 1, script 3 (compulsory part only)
# Author   : Dave Langers (c) 2020


# Initialise variables
linelength = 50

# Get filenames from user
print('Please enter your input file(s), separated by spaces:')
inputnames = input('? ')
inputnames = inputnames.split()
print('Please enter your output file:')
outputname = input('? ')
print()

# Open output file for writing
outputfile = open(outputname, 'w')

# For each input file, read contents and write reformatted output
for inputname in inputnames:
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
    # Write header and sequence to output file
    print(header, file=outputfile)
    for startposition in range(0, len(sequence), linelength):
        print(sequence[startposition:startposition+linelength], file=outputfile)
    print(file=outputfile)   # Add empty line before next sequence

# Close output file for writing
outputfile.close()

# Report results to the screen
print('Sequence(s) were successfully written to', outputname, 'using line-length', linelength)
