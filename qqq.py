ordate =[{'Пол':['Пол Аризин','197']},{'Боб':['Боб Коузи','197']}]
def funk_add():
    name = str(input("Имя"))
    height = float(input("рост"))
    data =  str(input("фио"))
    ordate.append([{name: [data,f'{height}']}])
    print(ordate)
    
def funk_delete():
    print('кого хотите удалить ')
    delin()
def delin():
    u =1
    for j in ordate:
        for i in j.values():
            print('номер ',u,sep=' ')
            print(i[0])
            u+=1
    date=int(input())
    ordate.pop(date-1)
    print(ordate)

def funk_sea():
    u =1
    for j in ordate:
        for i in j.values():
            print('номер ',u,sep=' ')
            print(i[0],i[1])
            u+=1
def funk_remuf():
    print('кого замените')
    delin()
    funk_add()







# def show(bd, name):
#     for i in bd:
#         if bd[i]['name'] == name:
#             return bd[i]
# def add_player(bd, name, age, number):
#     bd[len(bd)] = {'age':age, 'number': number, 'name':name}
#     return bd
# def del_player(bd, name):
#     for i in bd:
#         if bd[i]['name'] == name:
#             del(bd[i])
#             return bd
# bd = {0:{'age':'63', 'number':'88', 'name':'Jordan'},1:{'age':'43', 'number':'90', 'name':'Obi-Wan Kenobi'}}
# while True:
#     print('Список лучших')
#     for i in bd:
#         print(bd[i]['name'])
#     print('МЕНЮ: 1 - просмотреть полные данные \n 2 - добавить легенду\n 3 - удалить легенду')
#     token = input('Введите команду')
#     if token == '1':
#         name = input('Введите имя из списка для просмотра')
#         print(show(bd, name))
#     elif token == '2':
#         name = input('Введите имя для добавления')
#         age = input('Введите возраст для добавления')
#         number = input('Введите игровой номер для добавления')
#         add_player(bd, name, age, number)
#     elif token == '3':
#         name = input('Введите имя для удаления')
#         del_player(bd, name)