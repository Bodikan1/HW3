students = {}
num_students = int(input('Яка кількість учнів?: '))

#вхідні значення
for i in range(num_students):
    name = input('Вкажіть ім\'я учня: ')
    marks = int(input(f'Вкажіть оцінку учня {name}: '))
    pass_exam = input('Чи здав учень екзамен? Typing passed/failed: ')
    students[name] = marks, pass_exam

#перевірка на здав/не здав
for name, (marks, pass_exam) in students.items():
    if marks <= 100 and marks >= 75 and pass_exam == 'passed':
        print(f'Так, учня {name} оцінили правильно')
    elif marks <= 74 and marks >= 60 and pass_exam == 'failed':
        print(f'Так, учня {name} оцінили правильно')
    elif marks <= 59:
        print('Оцінка менше 60 та недопущена до оцінювання')
    else:
        print(f'Щось не так у {name}, спробуйте ще раз')

"""#перевірка на послідовність
for name, (marks, pass_exam) in students.items():
    if (marks <= 100 and marks >= 75 and pass_exam == 'failed') or (marks <= 74 and marks >= 60 and pass_exam == 'passed'):
        print ('Професорв не послідовним<<<<<'.upper())
    else:
        print('>>>>>Професорв був послідовним<<<<<'.upper())"""

# Перевірка на послідовність
checking = True
for name, (marks, pass_exam) in students.items():
    if (marks >= 75 and pass_exam != 'passed') or (marks < 75 and pass_exam != 'failed'):
        checking = False
        break

if checking:
    print('Професор був послідовним'.upper())
else:
    print('Професор не послідовний'.upper())


print('Дані учнів: ', students)

#діапазон оцінок
marks_list = []
for marks, pass_exam in students.values():
    marks_list.append(marks)

min_mark = min(marks_list)
max_mark = max(marks_list)

print(f'Діапазон оцінок: {min_mark}-{max_mark}')



