from unittest.mock import patch
from task_manager import add_task, get_tasks,list_tasks, complete_task, save_tasks, print_bold
import pytest
from unittest.mock import patch


@pytest.fixture
def mock_tasks():
    with patch('task_manager.load_tasks', return_value=[]) as mock_load_tasks, \
         patch('task_manager.save_tasks') as mock_save_tasks, \
         patch('task_manager.print_bold') as mock_print_bold, \
         patch('task_manager.get_tasks', return_value=([],[])) as mock_get_tasks, \
         patch('task_manager.input', return_value='Test task') as mock_input:
        yield mock_load_tasks, mock_save_tasks, mock_print_bold, mock_get_tasks, mock_input


def test_add_task_success(mock_tasks):
    mock_load_tasks, mock_save_tasks, mock_print_bold, mock_get_tasks, mock_input = mock_tasks
    add_task()
    mock_save_tasks.assert_called_once_with([{'id': 1, 'description': 'Test task', 'completed': False}])
    mock_print_bold.assert_called_once_with('Task added: Test task')

def test_add_task_failure(mock_tasks):
    mock_load_tasks, mock_save_tasks, mock_print_bold, mock_input = mock_tasks
    mock_input.return_value = ''
    with pytest.raises(ValueError):
        add_task()

def test_complete_task(mock_tasks):
    mock_load_tasks, mock_save_tasks, mock_print_bold, mock_input = mock_tasks
    task={'id': 1, 'description': 'Test task', 'completed': False}
    mock_load_tasks.return_value = [task]
    mock_input.return_value = '1'
    complete_task(task)
    mock_save_tasks.assert_called_once_with([{'id': 1, 'description': 'Test task', 'completed': True}])

