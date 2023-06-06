import yaml
from yaml.loader import SafeLoader
import click

@click.group(chain = True)
def main():
    pass

@main.command()
@click.argument('file_name')
def list(file_name:str):
    try:
        with open(f'{file_name}.yaml') as f:
            data = yaml.load(f, Loader=SafeLoader)
    except:
        print('Нет такого файла')
        return
    print(f"List of available {file_name}:")
    if file_name == 'tasks':
        for i in range(len(data['tasks'])):
            print(f"*{data['tasks'][i]['name']}")
    elif file_name == 'builds':
        for j in range(len(data['builds'])):
            print(f"*{data['builds'][j]['name']}")
    else:
        print('Нет такого файла')

@main.command()
@click.argument('file_name')
@click.argument('name')
def get(file_name:str, name:str):
    list_dependencies = []
    list_tasks =[]
    with open('builds.yaml') as f:
        builds = yaml.load(f, Loader=SafeLoader)
    with open('tasks.yaml') as f:
        tasks = yaml.load(f, Loader=SafeLoader)
    print(f"{file_name} info:")
    if file_name == 'builds':
        for item in builds['builds']:
            if item['name'] == name:
                list_tasks.extend(item.get('tasks'))
            else:
                print('Нет такого билда')
                return
        for j in item.get('tasks'):
            for i in tasks['tasks']:
                if i['name'] == j:
                    list_dependencies.extend(i['dependencies'])
        print('Name:', name,"\n", 'Tasks:', *list_dependencies+list_tasks)
    elif file_name == 'tasks':
        for item in tasks['tasks']:
            if item['name'] == name:
                print('Name', name,"\n","Dependencies:", *item.get('dependencies'))
            else:
                print('Нет такой таски')
                return
    else:
        print('Нет такой опции')

if __name__=='__main__':
    main()
