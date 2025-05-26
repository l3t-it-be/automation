import math


def calculate_formula(formula_text, x_text):
    formula_start = formula_text.find('ln')
    formula_end = formula_text.find(',')
    formula = formula_text[formula_start:formula_end].strip()

    result = eval(
        formula.replace('ln', 'math.log')
        .replace('sin', 'math.sin')
        .replace('x', x_text),
        {'math': math},
    )

    return result
