'''2) Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
  имя, фамилия, год рождения, город проживания, email, телефон.
   Функция должна принимать параметры как именованные аргументы.
   Реализовать вывод данных о пользователе одной строкой.       '''


def data_user(name, surname, old, city, email_u, phone):#(**kwargs)
    print(f'{name} {surname} {old} года рождения,'       #rpint(kwargs)
          f'Проживает в {city},email: {email_u},Телефон {phone}')


data_user(
    name='Кирилл',
    surname='Громов',
    old='1977',
    city='Омске',
    email_u='kain@gmail.com',
    phone='8904577999')
