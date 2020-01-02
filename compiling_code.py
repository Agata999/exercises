import math
import time

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []
for i in range(100000):
    argument_list.append(i/10)

for formula in formulas_list:
    print(f'Formula: {formula}')
    results_list = []
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
    minimum = min(results_list)
    maximum = max(results_list)
    print(f'Min value:{minimum}, max value:{maximum}')
    stop = time.time()
    time_without_compiling = stop - start
    print(f'Calculation time without compiled formula {formula} is: {time_without_compiling :2.3f}')
    print('-' * 30)

for formula in formulas_list:
    print(f'Formula: {formula}')
    results_list = []
    start = time.time()
    compiled_formula = compile(formula, formula, 'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    minimum = min(results_list)
    maximum = max(results_list)
    print(f'Min value:{minimum}, max value:{maximum}')
    stop = time.time()
    time_without_compiling = stop - start
    print(f'Calculation time with compiled formula {formula} is: {time_without_compiling :2.3f}')
    print('-' * 30)
