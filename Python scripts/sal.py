import re
import sys
import numpy as np

if __name__ == "__main__":
    filename = ''
    if len (sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print('Error: add path to filename!')

    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        
        number_list = []
        #получение всех выплат из файла
        for line in lines:
            number = re.search(r'.*(?=[\₽])', line, re.IGNORECASE)
            if number:
                number_list.append(number.group(0))
        #добавление символа '.' вместо ',', для конвертирования строки в float
        for id, number in enumerate(number_list):
            number = re.sub(r',', r'.', number, re.IGNORECASE)
            if number:
                number_list[id] = number
        #конвертирование списка строк в список float
        number_list = list(np.float_(number_list))
        #сумма полученных чисел
        print('Общий доход = {:,.2f}₽'.format(sum(number_list)))