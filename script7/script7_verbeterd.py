# Exercise: Theme 1, Script 7
# Date: was het 6 okt?

# Dit was een lijst doordat je [] gebruikte, moet {} zijn.
test_dict = {"test": "101 0100", "a": "100 0001", "c": "100 0011", "m": "110 0111", "w": "101 0111"}


def read_file():
    files = open("cf.gb")
    return files


def read_secs():
    section_dict = {}
    files = open("cf.gb", "r")
    for line in files:
        # Geen strip want dat haalt alle whitespaces weg
        if line == "\n":  # Om errors met lege lines te voorkomen
            pass
        elif not line.startswith(" "):  # Check of de line begint met een whitespace, zo ja, sla m over
            print(line.split()[0])
            section = line.split()[0]  # Pak het eerste woord van de zin (naam van key)
            section_dict[section] = line.split()[1:]  # Voeg de rest van de line toe aan de value van de dict
        else:
            section_dict[section].append(line)  # Voeg de rest van de content toe aan de vorige key
    print(section_dict)

read_this = """
je hebt t legit zitten te veranderen?!
ik appreciate dit wel maar werkt dit legit? o.o
"""



read_secs()

# nog wat functies
