employee = {
    'name' : 'Даниил',
    'salary' : 200
}

print(f'У {employee["name"]} зарплата в месяц = {employee["salary"]}')

emploee_list = [
    { 
    'name' : 'Даниил',
    'salary' : 200
    },
    {
    'name' : 'Егор',
    'salary' : 180
    },
    {
    'name' : 'Павел',
    'salary' : 150
    }
]

print(emploee_list[0])
for emploee in emploee_list:
    print(f'Имя: {emploee["name"]}, зарплата: {emploee["salary"]}')


#удаление
print(emploee_list)
for employee in emploee_list:
    if employee['name'] == 'Даниил':
        emploee_list.remove(employee)
        break

print(emploee_list)

#добавление
new_employee = {
    'name' : 'Кирилл',
    'salary' : 120
}

emploee_list.append(new_employee)
print(emploee_list)

print(f'Кол-во сотрудников в отделе: {len(emploee_list)}')


class Employee:
    def __init__(self, name, salary, on_vacation, is_good_employee):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
        self.is_good_employee = is_good_employee

    def get_info(self):
        return f'У {self.name} зарплата в месяц = {self.salary}. В отпуске? - {self.on_vacation}. Хороший работник? - {self.is_good_employee}'
    

employees = [Employee('Даниил', 200, True, True), Employee('Егор', 220, False, True), Employee('Павел', 190, False, True), Employee('Дмитрий', 170, False, True), Employee('Максим', 50, False, False)]

for employee in employees:
    if employee.is_good_employee == False:
        print(employee.get_info(), '(Уволен)')
        employees.remove(employee)
    else:
        print(employee.get_info())
