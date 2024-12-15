from FastaReader import FastaReader
from BasicOperations import BasicOperations


'''Считываем нуклеотидную последовательность из FASTA-файла'''

# Примеры Accession numbers:
# PP694298.1 - горноазиатский сурок Marmota baibacina, фрагмент рРНК большой рибосомальной субъединицы

'''dna - это переменная, в которую записывается нуклеотидная последовательность из файла'''

accession_number = input("Введите accession number: \n")
instance_FastaReader = FastaReader(accession_number)
dna = instance_FastaReader.read_file()


'''
dna_instance - это объект класса BasicOperation, 
для которого мы будем вызывать имеющиеся в классе методы.
В него передаём переменную dna.
'''

dna_instance = BasicOperations(dna)


'''
Проверяем последовательность на наличие ненуклеотидных элементов
* Функция возвращает 2 объекта и мы распаковываем их в 2 переменных
(это понадобится для записи в файл)
'''
validation_message, non_nucl_dict = dna_instance.validate_sequence()
print(validation_message, non_nucl_dict)


'''Считаем количественное содержание нуклеотидов в  последовательности'''

nucleotide_content = dna_instance.count_nucleotides()
print(f"Количественное содержание нуклеотидов в последовательности: {nucleotide_content}")


'''Получаем матричную РНК для заданной последовательности'''

coding_RNA = dna_instance.transcribe_to_RNA()
print(f"Матричная РНК для данной последовательности: {coding_RNA}")


'''Получаем reverse complement (обратную комплементарную цепь от 5' к 3' концу'''

reverse_complement_sequence = dna_instance.make_reverse_complement()
print(f"Обратная комплементарная цепью для заданной последовательности: {reverse_complement_sequence}")

def write_results_to_file():
    with open(f"{accession_number}.txt", "a+", encoding='utf8') as f:
        f.write(f"Результат анализа последовательности {accession_number}:\n {dna}\n")
        f.write(f"1. Результат проверки на наличие ненуклеотидных элементов:\n {validation_message}\n")
        f.write(f"2. Cписок обнаруженных ненуклеотидных элементов с позициями:\n {str(non_nucl_dict)}\n")
        f.write(f"3. Количественное содержание нуклеотидов в последовательности:\n {nucleotide_content}\n")
        f.write(f"4. Матричная РНК для заданной последовательности:\n {coding_RNA}\n")
        f.write(f"5. Обратная комплементарная цепь для заданной последовательности:\n {reverse_complement_sequence}\n")

if __name__ == "__main__":
    write_results_to_file()
