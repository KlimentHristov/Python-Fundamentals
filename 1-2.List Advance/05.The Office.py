def average(numbers):
    return sum(numbers) / len(numbers)

def solve(employees_string, happiness_factor_string):
    employees = list(map(int, employees_string.split(' ')))
    employees_count = len(employees)
    happiness_factor = int(happiness_factor_string)
    employees = list(map(lambda employee:employee*happiness_factor, employees))
    average_happiness = average(employees)
    happy_employees_count = len(list(filter(lambda employee: employee >= average_happiness, employees)))

    if happy_employees_count < employees_count // 2:
        print(f'Score: {happy_employees_count}/{employees_count}. Employees are not happy!')
    else:
        print(f'Score: {happy_employees_count}/{employees_count}. Employees are happy!')

solve(input(),input())