open_np = open("ccr5_np.fasta")
open_nc = open("ccr5_nc.fasta")

files = [open_np, open_nc]
results = []

#if you want to remove file_name input just comment from here till line 24
files = []
try:
    files.append(open(input("Enter the file name (with the extension): ")))
except FileNotFoundError:
   print("No such file was found in the directory of the project")
while True:
    question = input("Do you want to input another file? (y/n) ")
    if question == "n":
        break
    elif question=="y":
        try:
            files.append(open(input("Enter the file name (with the extension): ")))
        except FileNotFoundError:
            print("No such file was found in the directory of the project")
    else:
        print("Incorrect Input...")
# end of file_name input functionality



#def draw_graph(dict):
#    elements_count = sum(dict.values())
#    for key in dict:
#        value_perc = dict[key]/elements_count*100
#        print(key,"#"*round(value_perc), f"({value_perc}%)") # Remove f"({value_perc}%)" if you want the percentage off

def is_dna(element):
    string = ["A", "T", "C", "G"]
    if element not in string:
        return False
    return True

def count_acids(file):
    dna = True
    dict = {}
    for line in file:
        line = line.strip()
        if not line.startswith(">"):
            for element in line:
                if element in dict:
                    dict[element] += 1
                else: dict[element] = 1
                if dna:
                    dna = is_dna(element)
    return dict,dna

def calculate_CG_perc(dict):
    return (dict['C'] + dict['G'])/(sum(dict.values()))*100

for file in files:

    dict,dna = count_acids(file)
    results.append([dict,dna])

for result in results:
    print("---------------------------------------------")
    print(files[results.index(result)].name)
    print(result[0])
    print(f"Is the above sequnce a DNA: {result[1]}")
    if result[1]:
        print(f"CG% = {calculate_CG_perc(result[0])}%")
#    draw_graph(result[0])



