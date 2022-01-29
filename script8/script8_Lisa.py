# Exercise: Theme 1, script 8
# Author: Lisa Hu

# initialising variables
amino_codes = {
    'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
    'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
    'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
    'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'
}

# start code


def get_pdb(file_n):
    """
    Function tries to open the file (input)
    Parameter:
        name of the file (input)
    Return:
        opened pdb file
    """
    try:
        file_ = open(file_n+".pdb")
    except FileNotFoundError:
        print("File was not found")
    return file_


def get_fasta(file_n):
    """
    Function tries to open the file (input)
    Parameter:
        name of the file (input)
    Return:
        opened fasta file
    """
    try:
        file_ = open(file_n+".fasta")
    except FileNotFoundError:
        print("File was not found")
    return file_


def file_formatting(sequence):
    """
    Function prints sequence in format of 70 characters per line
    Parameter:
        sequence that needs to be printed
    """
    right_line = ""
    for start in range(0, len(sequence), 70):
        right_line += sequence[start:start+70] + "\n"

    return right_line


def get_content_pdb(file_):
    """
    Function looks for the protein sequence and puts it in a list
    Parameter:
        the opened file
    Return:
        list of amino acids
    """
    amino_list = []
    for line in file_:
        if line.startswith("SEQRES"):
            line = line.split()
            for i in line:
                if i in amino_codes:
                    amino_list.append(i)

    file_.close()
    return amino_list


def count_pro(protein):
    """
    Function counts each protein in sequence and returns it in a dictionary
    Parameter:
        the sequence that needs to be counted
    Return:
        dictionary with proteins (keys) and amounts (values)
    """
    histo_dict = {}
    for char in protein:
        if char not in histo_dict:
            histo_dict[char] = 1
        else:
            histo_dict[char] += 1

    return histo_dict


def make_histogram(histo_dict):
    """
    Function makes histogram in terminal
    Parameter:
        dictionary with proteins and their amounts
    Return:
        histogram
    """
    histogram = str()
    for i in histo_dict:
        if histo_dict[i] > 50:
            histogram = i, "#" * histo_dict[i]/10, "(x10), precise: ", histo_dict[i]
        else:
            histogram = i, "#" * histo_dict[i]

    return histogram


def abbrev_translate(amino_list):
    """
    Function translates 3 letter amino acid into 1 letter amino acid
    Parameter:
        list of amino acids of the file
    Return:
        protein sequence
    """
    protein = ""

    for amino in amino_list:
        if amino not in amino_codes:
            pass
        else:
            protein += amino_codes[amino]

    return protein


def get_helix_sheet(file_name, protein):
    """
    Function gets protein sequence of the helix's and sheets
    Parameters:
        name of the file (input)
        protein sequence
    """
    sheet = ""
    helix = ""
    file_ = get_pdb(file_name)

    for line in file_:
        if line.startswith("HELIX"):
            if line.split()[3] not in amino_codes:              # skip de UNK's
                pass
            else:
                init_seq_int = int(line.split()[5]) - 1         # start position in protein
                end_seq_int = int(line.split()[8])              # end position in protein
                helix += protein[init_seq_int:end_seq_int]      # slicing in protein and putting them together

        elif line.startswith("SHEET"):
            init_seq = int(line[22:26].strip()) - 1     # same procedure and obtaining helix
            end_seq = int(line[33:37].strip())
            sheet += protein[init_seq:end_seq]

    file_.close()

    return helix, sheet


def compare_seq(fasta_file, pro_seq):
    fasta_pro = ""
    for line in fasta_file:
        if not line.startswith(">"):
            fasta_pro += line.strip()

    # zipped = zip(fasta_file, pro_seq)
    # for char
    return


def main():
    """
    Main function
    """
    file_name = input("Enter abbreviation of disease (no extension needed): ")  # user gives name of wanted file
    open_pdb = get_pdb(file_name)
    amino_list = get_content_pdb(open_pdb)
    pro_seq = abbrev_translate(amino_list)
    open_fasta = get_fasta(file_name)
    compare_seq(open_fasta, pro_seq)

    helix, sheet = get_helix_sheet(file_name, pro_seq)

    print("- PROTEIN sequence:", "\n", pro_seq)
    print(make_histogram(pro_seq))
    print("- HELIX sequence:", "\n", file_formatting(helix))
    print(make_histogram(helix))
    print("- SHEET sequence:", "\n", file_formatting(sheet))
    print(make_histogram(sheet))


main()

"""
pep 8
benaming
meer return
vergelijking van protein
"""