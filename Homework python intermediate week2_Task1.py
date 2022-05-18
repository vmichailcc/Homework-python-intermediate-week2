class FormulaError(Exception):
    pass


def calc(input_line):
    line = input_line.split(' ')
    try:
        if len(line) == 3:
            if line[1] in ('+', '-', '*', '/'):
                try:
                    num1 = float(line[0])
                    num2 = float(line[2])
                except ValueError:
                    print(f'{input_line} - Ошибка ввода. Введите число')
            else:
                raise FormulaError
        else:
            raise FormulaError
    except FormulaError:
        print(f'{input_line} - Ввод не состоит из 3 элементов или введен неправильный оператор')

    try:
        if line[1] == '+':
            answer_calc = num1 + num2
        if line[1] == '-':
            answer_calc = num1 - num2
        if line[1] == '*':
            answer_calc = num1 * num2
        if line[1] == '/':
            answer_calc = num1 / num2
        return f'\tРезультат операции {input_line} = {answer_calc}'
    except UnboundLocalError:
        return f'{input_line} Неправильный ввод данных \n'


print(calc('y + 1'))
print(calc('8 - p'))
print(calc('7 7 7'))
print(calc('55 / 7'))
print(calc('6 * 55 + 8'))
print(calc('1 + 1'))
