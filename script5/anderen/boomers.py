codon_dict = {
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
    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}


# endregion


def main():
    frequency_dict = {}
    output_file = open("output.txt", 'w')
    fasta_output_file = open("TRANS.fasta", 'w')
    while not check_stop():
        file_name = input("wat is de naam van je mRNA fasta?") + ".fasta"
        file_handler = open(file_name)
        aminos = get_frequency(file_handler, frequency_dict)
        most_frequent = get_most_frequent_amino(frequency_dict)
        write_output(output_file, file_name, most_frequent)
        file_handler.close()

        convert_fasta(aminos, most_frequent, fasta_output_file, file_name)

        frequency_dict = {}

    output_file.close()


def convert_fasta(sequence, most_frequent, output, file_name):
    to_write = ""
    counter = 0
    temp = ""
    for letter in sequence:
        codon = most_frequent[letter]
        temp += codon
    for letter in temp:
        to_write += letter
        counter += 1
        if counter == 70:
            to_write += "\n"
            counter = 0
    print(file_name, file=output)
    print(to_write, file=output)


def write_output(output_file, file_name, most_frequent):
    print(file_name, file=output_file)
    for key in most_frequent:
        to_print = key + "             " + most_frequent[key]
        print(to_print, file=output_file)
    print(file=output_file)


def check_stop():
    while True:
        print("Wil je stoppen?(j/n)")
        answer = input()
        if answer == 'j':
            return True
        elif answer == 'n':
            return False


def get_most_frequent_amino(frequency_dict):
    my_dict = {}
    for triplet in frequency_dict:
        try:
            current_amino = codon_dict[triplet]

            existing_frequency = frequency_dict[my_dict[current_amino]]
            new_frequency = frequency_dict[triplet]

            if existing_frequency < new_frequency:
                my_dict[current_amino] = triplet
        except:
            my_dict[codon_dict[triplet]] = triplet
    return my_dict


def get_frequency(handler, frequency_dict):
    sequence = ""
    aminos = ""
    for line in handler:
        line = line.rstrip()
        if line.startswith('>'):
            continue
        sequence += line
        codon = ""
        for letter in line:
            codon += letter
            if len(codon) != 3:
                continue
            aminos += codon_dict[codon]

            try:
                frequency_dict[codon] += 1
            except:
                frequency_dict[codon] = 1
            codon = ""
    return aminos


main()