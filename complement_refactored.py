
#Devin Keller
#2368610
#Dkeller@chapman.edu
#CPSC-230-09
#Assignment 9 exercise 1

def get_DNA(Filename):
    DNAlist = []
    try:
        DNAFile = open(Filename)
    except(IOError):
        print("File Cannot be found")
    content = DNAFile.readlines()

    for i in content:
        DNAlist.append(i)
    
    global DNA
    DNA = []
    DNAFile.close()
    for i in DNAlist:
        for n in i:
            DNA.append(n)



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
        elif i == '\n':
            RNA.append('\n')
        else:
            raise ValueError("Unknown Character in file")
    global RNA_str
    RNA_str = ''
    for i in RNA:
        RNA_str += i



def rev_complement(RNA_str):
    global rev_RNA
    rev_RNA = RNA_str[::-1]
    rev_RNA = "Reverse Complement: " + rev_RNA


def results(rev_RNA, RNA_str):
    results = open('results.txt', 'a')
    results.write('Complement: ')
    results.write(RNA_str)
    results.write('\n')
    results.write(rev_RNA)

    results.flush()
    results.close()

print()
Filename = input("Filename: ")
    
get_DNA(Filename)
complement(DNA)
rev_complement(RNA_str)
results(rev_RNA, RNA_str)

