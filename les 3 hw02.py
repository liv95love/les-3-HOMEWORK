    name = input('input name')
    surname = input('Введите фамилию')
    year = int(input('Введите год рождения'))
    city = input('Введите город')
    email = input('Введите email')
    telephone = input('input telephone')
def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Goryacheva', name = 'Lyubov', year = '1995', city = 'Samara', email = '123@mail.ru', telephone = '8800555555'))