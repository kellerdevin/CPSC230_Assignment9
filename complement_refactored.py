def complement(DNA):
    
    RNA = []
    for i in DNA:
        if i == 'A':
            RNA.append('T')
        elif i == 'T':
            RNA.append('A')
        elif i == 'C':
            RNA.append('G')
        elif i == 'G':
            RNA.append('C')
        else:
            print("Error")
            exit()
    global RNA_str
    RNA_str = ''
    for i in RNA:
        RNA_str += i

    global RNA_str_results
    RNA_str_results = 'Complement: ' + RNA_str



def rev_complement(RNA_str):
    global rev_RNA
    rev_RNA = ''
    rev_RNA = RNA_str[::-1]
    rev_RNA = "Reverse Complement: " + rev_RNA


def results(rev_RNA, RNA_str_results):
    results = open('results.txt', 'a')
    results.write('Complement: ')
    results.write(RNA_str_results)
    results.write('\n')
    results.write(rev_RNA)

    results.flush()
    results.close()

print()
DNA= input("Input DNA sequence: ")
DNA = DNA.upper()
for i in DNA:
    if i != 'A' or i != 'C' or i != 'G' or i != 'T':
        raise ValueError('Unknown character entered')

    

complement(DNA)
rev_complement(RNA_str)
results(rev_RNA, RNA_str)

