
class BasicOperations:
    """Класс содержит функции с базовыми операциями для анализа цепи ДНК"""
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.nucleotides = ["A", "T", "G", "C"]
        self.complementary_nucleotides = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
        self.garbage_dict = {}
        self.mRNA = ""


    def validate_sequence(self):
        """
        Функция проверяет, содержатся ли в последовательности ДНК элементы,
        не являющиеся нуклеотидами.

        Возвращает сообщение с результатом проверки
        и словарь с ненуклеотидными элементами и их позициями.
        """
        messages = []
        for index, nucl in enumerate(self.sequence):
            if nucl in self.nucleotides:
                pass
            elif nucl not in self.nucleotides:
                self.garbage_dict[nucl] = index
                messages.append(f"Обнаружен ненуклеотидный элемент {nucl} на позиции {index}!")

        if self.garbage_dict == {}:
            messages.append("Данная последовательность является ДНК")

        validation_messages = '\n'.join(messages)
        return validation_messages, self.garbage_dict


    def count_nucleotides(self):
        """
        Функция считает количественное содержание нуклеотидов в цепи ДНК.

        Возвращает словарь, в котором указано количество
        каждого из нуклеотидов.
        """
        self.count_dict = {}
        for nucl in self.sequence:
            if nucl in self.count_dict:
                self.count_dict[nucl] += 1
            else:
                self.count_dict[nucl] = 1
        return self.count_dict


    def transcribe_to_RNA(self):
        """
        Функция воспроизводит процесс транскрипции ДНК в РНК.
        На вход берётся кодирующая цепь.

        Поскольку синтез РНК идёт комплементарно с матричной цепи (template strand),
        РНК будет совпадать с последовательностью кодирующей цепи (coding strand),
        за исключением того, что тимин(T) заменится на урацил(U).

        Функция возвращает цепь РНК для кодирующей цепи.
        """
        self.mRNA = self.sequence.replace("T", "U")
        return self.mRNA


    def make_reverse_complement(self):
        """
        Функция воспроизводит процесс репликации ДНК.
        На вход берётся кодирующая цепь.

        С неё в обратном порядке (от конца к началу)
        синтезируется комплементарная цепь.

        Функция возвращает цепь, комплементарную исходной
        и развёрнутую в противоположном направлении.
        """
        self.reversed_complement = ''.join([self.complementary_nucleotides[nucl] if nucl in self.complementary_nucleotides else nucl for nucl in self.sequence[::-1]])
        return self.reversed_complement


