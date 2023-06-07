program for Saber
------------
для работы скрипта нужно выполнить команды в консоли:

    pip install pyyaml #пакет для работы с yaml
    pip install click #пакет для создания CLI

Скрипт обрабатывает файлы tasks.yaml и builds.yaml 

Созданы две функции:
list(file_name) и get(file_name, name)

list()
---------------------------------------
list() принимает аргумент типа string, который обозначает имя обрабатываемого файла, и выводит:

если file_name = builds, то список билдов

если file_name = tasks, то список задач

get()
---------------------------------------
get() принимает два аргумента типа string: file_name - имя файла(tasks или builds) и name(имя нужного билда или задачи)

если file_name = builds, то выводит список задач для билда(name), учитывая зависимости каждой задачи

если file_name = tasks, то выводит список зависимостей задачи(name)

CLI
---------------------------------------

функции скрипта вызываются через консоль посредством click(пакет для создания CLI)

вызов функции list():
    python main.py list file_name, где file_name - имя обрабатываемого файла
вызов функции get():
    python main.py get file_name name, где file_name - имя обрабатываемого файла, name - имя нужного билда или задачи

Тесты
---------------------------------------
тесты находятся в файле tests.py, запуск через консоль:

pytest.exe tests.py

Список тестов:

1) test_is_tasks_exist - тест на наличие файлa tasks.yaml 
2) test_is_builds_exist - тест на наличие файлa builds.yaml
3) test_is_empty_file_tasks - тест на пустоту файла tasks.yaml
4) test_is_empty_file_builds  - тест на пустоту файла builds.yaml 
5) test_is_task_exists - тест на наличие тасков файле tasks.yaml
6) test_is_build_exists - тест на наличие билдов в файле builds.yaml
