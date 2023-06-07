import pytest
import yaml
from yaml.loader import SafeLoader
from main import get, list
import os

def test_is_tasks_exist():
    assert os.path.isfile('tasks.yaml') == True
def test_is_builds_exist():
    assert os.path.isfile('builds.yaml') == True
def test_is_empty_file_builds():
    assert os.stat("builds.yaml").st_size != 0
def test_is_empty_file_tasks():
    assert os.stat("tasks.yaml").st_size != 0
def test_is_task_exists():
    with open('tasks.yaml') as f:
        tasks = yaml.load(f, Loader=SafeLoader)
    list_tasks = [item['name'] for item in tasks['tasks']]
    assert 'map_gray_centaurs' in list_tasks
def test_is_build_exists():
    with open('builds.yaml') as f:
            builds = yaml.load(f, Loader=SafeLoader)
    list_builds = [item['name'] for item in builds['builds']]
    assert 'time_alone' in list_builds