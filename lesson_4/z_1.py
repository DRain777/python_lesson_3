name = 'Nikolay'
work_h = 120
pay_h = 27
bonus = 4000


def cal_salary(name, work_h, pay_h, bonus):
    res = work_h * pay_h + bonus
    print(f'Сотрудник {name} зарплата: часы {work_h}$'
          f' * оклад {pay_h}$ + премия {bonus}$ = {res}$')


cal_salary(name, work_h, pay_h, bonus)
