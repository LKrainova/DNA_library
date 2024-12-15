class FastaReader:
    def __init__(self, accession_number):
        self.accession_number = accession_number

    def read_file(self):
        with open(f"{self.accession_number}.fasta", "r+") as f: # PQ633951.1 # OQ324770.1
            lines = f.readlines()
            '''
            Убираем имеющиеся в FASTA-файле пробелы в конце строк.
            Читаем со второй строки. 
            '''
            dna_from_fasta = ''.join(line.strip() for line in lines[1:])
            print(dna_from_fasta)
            return dna_from_fasta




