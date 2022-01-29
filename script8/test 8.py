file_ = open("cf.pdb")
protein = "MQRSPLEKASVVSKLFFSWTRPILRKGYRQRLELSDIYQIPSVDSADNLSEKLEREWDRELASKKNPKLINALRRCFFWRFMFYG"

amino_codes = {
    'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
    'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
    'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
    'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'
}
def helix():
    for line in file_:
        if line.startswith("HELIX"):
            if line[15:18] not in amino_codes:  #skip de UNK's
                pass
            else:
                helix = ""
                initResName = line[15:18]
                endResName = line[27:30]
                initSeqInt = int(line[21:25].strip())
                endSeqInt = int(line[33:37].strip())
                helix += protein[initSeqInt:endSeqInt]
    return


"""
initResName = line[15:18]   (SER)
endResName = line[27:30]    (PHE)
initSeqInt = line[21:25]    (10)
endSeqInt = line[33:37]     (17)
"""

sheet = """
SHEET    2 AA1 2 GLU A 479  LYS A 483 -1  O  LYS A 483   N  VAL A 393
"""
line = sheet.split()

initResName = line[4]   # GLU
endResName = line[7]    # LYS
initSeqNum = line[6]    # 479
endSeqNum = line[9]     # 483
sense = line[10]        # 0 = first strand, 1 = parallel, -1 = anti-parallel

