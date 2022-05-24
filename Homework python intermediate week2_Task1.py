class FormulaError(Exception):
    pass


def calc(input_line):
    line = input_line.split(' ')

    if len(line) != 3:
        raise FormulaError('Ввод не состоит из 3 элементов')

    try:
        num1 = float(line[0])
        num2 = float(line[2])
    except ValueError:
        raise FormulaError('Ошибка ввода. Введите число')

    if line[1] not in ('+', '-', '*', '/'):
        raise FormulaError('Введен неправильный оператор')

    if line[1] == '+':
        answer_calc = num1 + num2
    if line[1] == '-':
        answer_calc = num1 - num2
    if line[1] == '*':
        answer_calc = num1 * num2
    if line[1] == '/':
        answer_calc = num1 / num2
    return f'Результат операции {input_line} = {answer_calc}'


print(calc("1 + 1"))
