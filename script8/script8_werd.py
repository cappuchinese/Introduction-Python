"""
Uitwerking van opdracht8
Autheur: Ronald Wedema
Date: oktober 2020
"""


def ask_input():
    """
    function to ask and return pdb input and fasta output file names
    """

    file_in_pdb, file_in_ncbi, file_out_fasta = \
        input("Please give: Pdb, ncbi and an outfile all separated by space: ").split()
    return file_in_pdb, file_in_ncbi, file_out_fasta


def read_fasta(fasta_file_name):
    """
    Deze functie leest een fasta
    :param fasta_file_name: name of a fasta fila as string
    :return:
    """

    fasta_handler = open(fasta_file_name)

    seq = ''

    for line in fasta_handler:
        line = line.strip()

        # ignore header only interested in the sequence
        if not line.startswith(">"):
            seq += line

    fasta_handler.close()

    return seq


def read_pdb(pdb_file_name):
    """
    Read a pdb file and store the SEQRES, HELIX and SHEET content into a dictionary
    """

    # pre define keys in the dict
    content_dict = {"SEQ": "", "HELIX": [], "SHEET": []}

    pdb_reader = open(pdb_file_name)

    for line in pdb_reader:
        if line.startswith("SEQRES"):
            content_dict["SEQ"] += line[19:]  # ignore first part of the line, contains numbers not part of the sequence
        if line.startswith("HELIX"):
            start = int(line[21:26])  # see pdb column notation for helix start and stop locations
            stop = int(line[33:38])
            content_dict["HELIX"].append((start, stop))
        if line.startswith("SHEET"):  # see pdb column notation for sheet start and stop locations
            start = int(line[22:27])
            stop = int(line[33:38])
            content_dict["SHEET"].append((start, stop))

    pdb_reader.close()

    return content_dict


def translate_amino_to_one_letter(seq):
    """
    Translate a 3-letter amino sequence to a 1-letter sequence
    """

    d = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K', 'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F',
         'ASN': 'N', 'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 'ALA': 'A', 'VAL': 'V', 'GLU': 'E',
         'TYR': 'Y', 'MET': 'M', 'UNK': '*'}

    one_letter_protein_seq = ""
    split_seq = seq.split()  # three letters seperated by space

    # loop over every three letters
    for three_letter in split_seq:
        # get single letter from dict and add to new single letter sequence
        one_letter_protein_seq += d[three_letter]

    return one_letter_protein_seq


def get_content(seq):
    """
    Given a sequence determine the freq of each letter/amino
    """

    comp_dict = {}

    # loop over every amino and add the count to the dict
    for amino in seq:
        if amino in comp_dict:
            comp_dict[amino] += 1
        else:
            comp_dict[amino] = 1

    return comp_dict


def compare_seq(pdb, ncbi, window):
    """
    Given two sequences and a window (size) show one sequence above the other
    Middle line printed: where - shows equal amino and * for mismatch amino
    """

    # determine the largest and smallest sequence
    largest = len(max(pdb, ncbi))
    smallest = len(min(pdb, ncbi))

    # what is the size difference
    size_dif = largest - smallest

    # define empty string to hold the comparison (equal or diff; | vs *)
    dif = ''

    # loop over the smalles sequence
    for position in range(0, smallest):
        # compare aminos from both sequences for this position
        if pdb[position] != ncbi[position]:  # amino's are not equal, add * symbol
            dif += "*"
        else:  # amino's are equal add | symbol
            dif += "|"

    # fill smallest sequence with mismatch symbol
    dif += '*' * size_dif

    # print two original sequences separated by the difference sequence, using the window size for sequence lengths
    for position in range(0, largest, window):
        print(pdb[position:position+window])
        print(dif[position:position+window])
        print(ncbi[position:position+window] + "\n")


def get_sequence(list_of_tuples, total_seq):
    """
    Return an extracted sequence from a given list of tuples
    tuples have start and stop respectively
    """

    # define new string to hold the extracted sequence
    seq = ''

    # loop over the tuples
    for start_stop_tuple in list_of_tuples:
        # get start and stop
        start = start_stop_tuple[0] - 1
        stop = start_stop_tuple[1]
        # slice the original sequence and add sliced portion to the seq variable
        seq += total_seq[start:stop]

    return seq


def draw_composition(seq):
    """
    For a given sequence draw the amino composition using a horizontal histogram
    """

    # get the sequence composition
    comp_dict = get_content(seq)

    # draw the freq using # for every 1% a single # is used (rounded to ignore decimal part)
    for every_amino in comp_dict:
        number_of_hashes_to_draw = "#" * round(comp_dict[every_amino] / len(seq) * 100)
        print(every_amino + ": " + number_of_hashes_to_draw)


def write_fasta(header, sequence, out_file_writer):
    """
    Write a fasta file using the version, definition and cleaned ORIGIN from the genbank file
    """

    print(">" + header, file=out_file_writer)

    # write lines of length 70 to the outfile
    for position in range(0, len(sequence), 70):
        print(sequence[position:position+70], file=out_file_writer)


def main():
    """
    One function to rule them all!
    """

    # ask user for input files
    file_in_pdb, file_in_ncbi, file_out_fasta = ask_input()

    # read the ncbi fasta sequence
    fasta_sequence = read_fasta(file_in_ncbi)

    # read the pdb file and save it to dict
    pdb_content_dict = read_pdb(file_in_pdb)

    # translate the 3-letter sequence to a 1-letter sequence
    pdb_content_dict["ONE_LETTER"] = translate_amino_to_one_letter(pdb_content_dict["SEQ"])

    # compare both sequences and show where they are similar or different
    compare_seq(pdb_content_dict["ONE_LETTER"], fasta_sequence, 200)

    # extract the helix and sheet sequence from the total sequence
    pdb_content_dict["HELIX_SEQ"] = get_sequence(pdb_content_dict["HELIX"], pdb_content_dict["ONE_LETTER"])
    pdb_content_dict["SHEET_SEQ"] = get_sequence(pdb_content_dict["SHEET"], pdb_content_dict["ONE_LETTER"])

    # print the histograms
    print("Total sequence composition ")
    draw_composition(pdb_content_dict["ONE_LETTER"])
    print("Helix sequence composition ")
    draw_composition(pdb_content_dict["HELIX_SEQ"])
    print("Sheet sequence composition")
    draw_composition(pdb_content_dict["SHEET_SEQ"])

    # write helix and sheet sequence to multi-fasta file
    fasta_writer = open(file_out_fasta, 'w')
    write_fasta("helix", pdb_content_dict["HELIX_SEQ"], fasta_writer)
    write_fasta("sheet", pdb_content_dict["SHEET_SEQ"], fasta_writer)
    fasta_writer.close()
    print("Multi fasta file written: " + file_out_fasta)


main()
