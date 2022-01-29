# Exercise : Theme 1, script 2 (compulsory part only)
# Author   : Dave Langers (c) 2020


# Initialise variables
inputname = 'CCR5_protein.fasta'
counter = 0
composition = dict()
is_nucleotide = True

# Read file contents and count numbers of nucleotides/aminoacids
inputfile = open(inputname, 'r')
for line in inputfile:
    line = line.rstrip()   # Remove newline character
    if not line.startswith('>'):   # Ignore file header
        counter += len(line)
        for character in line:
            if character not in 'ACTG':
                is_nucleotide = False
            if character in composition:
                composition[character] += 1   # Increase the existing count by +1
            else:
                composition[character] = 1   # Add a new entry with count 1
inputfile.close()

# Report results to the screen
if is_nucleotide:
    GC_percentage = (composition['G']+composition['C']) * 100 // counter
    print('The number of nucleotides in', inputname, 'equals', counter, '(GC =', GC_percentage, '%)')
else:
    print('The number of amino-acids in', inputname, 'equals', counter)
print('Sequence composition:')
for key in composition:
    print(key, '=', composition[key])
