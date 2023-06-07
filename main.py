import yaml
from yaml.loader import SafeLoader
import click

@click.group(chain = True) #
def main():
    pass

@main.command()
@click.argument('file_name')
def list(file_name:str):
    try:
        with open(f'{file_name}.yaml') as f:  #Открываем нужный файл
            data = yaml.load(f, Loader=SafeLoader)
    except:
        print('Нет такого файла')
        return
    print(f"List of available {file_name}:")
    if file_name == 'tasks':
        for i in range(len(data['tasks'])):
            print(f"*{data['tasks'][i]['name']}") #Вывод всех тасков
    elif file_name == 'builds':
        for j in range(len(data['builds'])):
            print(f"*{data['builds'][j]['name']}") #Вывод всех билдов

@main.command()
@click.argument('file_name')
@click.argument('name')
def get(file_name:str, name:str):
    list_dependencies = [] #Пустой список для хранения зависимостей тасков
    list_tasks =[] #Пустой список для хранения тасков
    count = 0 #Счетчик для проверки наличия билда или таска
    with open('builds.yaml') as f:
        builds = yaml.load(f, Loader=SafeLoader) #Открываем нужный файл
    with open('tasks.yaml') as f:
        tasks = yaml.load(f, Loader=SafeLoader) #Открываем нужный файл
    print(f"{file_name} info:")
    if file_name == 'builds':
        for item in builds['builds']:
            if item['name'] == name:
                count += 1 #Увеличиваем счетчик, если нашелся билд
                list_tasks.extend(item.get('tasks'))
                for j in item.get('tasks'):
                    for i in tasks['tasks']:
                        if i['name'] == j:
                            list_dependencies.extend(i['dependencies'])
        if count != 0:
            print('Name:', name,"\n", 'Tasks:', *list_dependencies+list_tasks) #Если найден билд, то вывод его тасков и зависимостей
        else:
            print('Нет такого билда')
    elif file_name == 'tasks':
        for item in tasks['tasks']:
            if item['name'] == name:
                count +=1 #Увеличиваем счетчик, если нашлась таска
            else:
                pass
        if count!=0:
            print('Name:', name, "\n", "Dependencies:", *item.get('dependencies')) #Если найдена таска, то вывод её зависимостей
        else:
            print('Нет такой таски')
    else:
        print('Нет такой опции')

if __name__=='__main__':
    main()

