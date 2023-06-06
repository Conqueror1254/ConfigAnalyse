import yaml
from yaml.loader import SafeLoader
import click


@click.group(chain = True)
def main():
    pass

@main.command()
@click.argument('file_name')
def list(file_name:str):
    with open(f'{file_name}.yaml') as f:
        data = yaml.load(f, Loader=SafeLoader)
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
    with open(f'{file_name}.yaml') as f:
        data = yaml.load(f, Loader=SafeLoader)
    print(f"{file_name} info:")
    if file_name == 'builds':
        for item in data['builds']:
            if item['name'] == name:
                print('Name:', name,"\n","Tasks:", *item.get('tasks'))
    elif file_name == 'tasks':
        for item in data['tasks']:
            if item['name'] == name:
                print('Name', name,"\n","Dependencies:",*item.get('dependencies'))
    else:
        print('Нет такой опции')

if __name__=='__main__':
    main()
