import csv

def find_role(name, data):
    '''
    Поиск по массиву
    :param name: Название вакансии
    :param data: Массив 
    :return: Dict(Со всей строчкой) or None
    '''
    for i in data:
        if i["Role"] == name:
            return i

    return None


inp = input('Введите название вакансии: ')
while inp.lower() != 'устал':
    with open('vacancy.csv', 'r', newline='', encoding='utf-8') as csvf:
        f = csv.DictReader(csvf, delimiter=';', quotechar='|')
        res = find_role(inp, f)
        if res is not None:
            print(f'В {res["Company"]} найдена искомая вакансия: {res["Work_Type"]}. З/п составит: {res["Salary"]}')
        else:
            print('К сожалению, ничего не удалось найти')
        inp = input('\nВведите название вакансии: ')

print('Stop')
