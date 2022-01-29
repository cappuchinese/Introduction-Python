# "AAAAA"
#  ||| |
# "AAAtA"

fasta_seq = "MHFHSOFBDJEFBEURYH"
pro_seq = "MHFHSOFBDJGFBEURTH"

zipped = zip(fasta_seq, pro_seq)
for char1, char2 in zipped:
    print(char1, char2)
    if char1 != char2:
        char2.replace(char2, char2.lower())
        print(char1, char2)