# Exercise: Theme 1, Script 5
# Author: Lisa Hu

# initiating variables
header = ""
sequence = ""
protein = ""
lines = ""
reverse = ""
rev_lines = ""
result = ""
codon_count = {}
new_dict = {}
reverse_dict = {}
codonlength = 3
dna_letters = "ACTG"
rna_file = open("trans.txt", "w")
output = open("output.txt", "w")

dna_codons = {
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

# start code
# function to open files
def input_files():
    try:
        files = open(input("Enter file name: "))
    except FileNotFoundError:
        print("File was not found")
    return files

# function to check if file contains DNA sequence
def dna_check():
    z = set(sequence)
    if bool(z.difference(set(dna_letters))) is True:
        return False
    return True

# function to print sequence in file
def results():
    results = header + "\n" + \
              "Protein sequence:" + "\n" + lines + "\n" + \
        "Most common triplet per amino acid:" + "\n" + result + "\n"
    print(results, file=output)

# user can give input for line length
try:
    line_length = int(input("Enter the line length: "))
except ValueError:
    print("Incorrect input")


while True:
    fil = input_files()     # opens file
    for line in fil:
        line = line.strip()     # strips line
        if line.startswith(">"):
            header = line       # stores header of the file
        else:
            sequence += line.upper()    # stores sequence of the file

    if dna_check():                                             # only works it if it's a DNA sequence
        for startpos in range(0, len(sequence), codonlength):   # goes through sequence in steps of 3
            codon = sequence[startpos:startpos + codonlength]   # stores triplet as codon
            if len(codon) == 3:                                 # codon needs to be three
                if not dna_codons[codon] in new_dict:           # checks if value of dna_codon is in new_dict
                    new_dict[dna_codons[codon]] = [codon]       # add to new_dict as list
                else:
                    if codon not in new_dict[dna_codons[codon]]:    # if the codon is not in the values of new_dict
                        new_dict[dna_codons[codon]].append(codon)   # append codon as value to the right key
                # count each triplet
                if codon not in codon_count:
                    codon_count[codon] = 1
                else:
                    codon_count[codon] += 1
                protein += dna_codons[codon]    # translate codon to amino acid and add to protein

        for key in new_dict:    # iterates through new_dict
            for triplet in new_dict[key]:   # iterates through values of new_dict
                if key in reverse_dict:
                    # if the counter of key's value is smaller than count of triplet
                    if codon_count[reverse_dict[key]] < codon_count[triplet]:
                        reverse_dict[key] = triplet     # add the triplet to reverse_dict with key
                else:
                    reverse_dict[key] = triplet

        for char in protein:   # iterate through protein per character
            reverse += reverse_dict[char]   # stores translated character as codon

        # stores protein sequence in given format
        for startposition in range(0, len(protein), line_length):
            lines += protein[startposition:startposition + line_length] + "\n"

        # stores reversed sequence in given format
        for startposition in range(0, len(reverse), line_length):
            rev_lines += reverse[startposition:startposition + line_length] + "\n"
        # print rna sequence to rna file
        print(header + "\n" + "Reversed sequence:" + "\n" + rev_lines + "\n", file=rna_file)

        # stores most used triplet per amino acid in result
        for key in reverse_dict:
            result += key + " : " + reverse_dict[key] + "\n"

        results()   # print final result

    else:   # print if file is not DNA
        print("File does not contain nucleotide sequence")

    # ask user for another input
    question = input("Do you want to open another file? (y/n) ")
    if question == "n":     # break if no
        print("Done")
        break
    elif question == "y":   # clear all variables and close previous file if yes
        header = ""
        sequence = ""
        protein = ""
        lines = ""
        reverse = ""
        rev_lines = ""
        result = ""
        codon_count = {}
        new_dict = {}
        reverse_dict = {}
        fil.close()
    else:
        print("Incorrect input")

output.close()  # close output file
