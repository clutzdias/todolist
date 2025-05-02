from app.exceptions import (
    TaskAlreadyExistsException,
    TaskNotFoundException
)
from werkzeug.exceptions import HTTPException


def test_create_task_success(task_service, sample_task):
    task_service.repository.get_task_by_title.return_value = None
    task_service.repository.create_task.return_value = sample_task

    result = task_service.create_task(sample_task)

    assert result.title == sample_task.title
    task_service.repository.create_task.assert_called_once()


def test_create_task_already_exists(task_service, sample_task):
    task_service.repository.get_task_by_title.return_value = sample_task

    try:
        task_service.create_task(sample_task)
    except HTTPException as e:
        assert isinstance(e, TaskAlreadyExistsException)


def test_get_task_success(task_service, sample_task):
    task_service.repository.get_task.return_value = sample_task

    result = task_service.get_task(1)

    assert result.title == sample_task.title
    task_service.repository.get_task.assert_called_once_with(1)


def test_get_task_not_found(task_service):
    task_service.repository.get_task.return_value = None

    try:
        task_service.get_task(99)
    except TaskNotFoundException as e:
        assert "not found" in str(e)


def test_update_task_success(task_service, sample_task):
    task_service.repository.get_task.return_value = sample_task
    task_service.repository.update_task.return_value = None

    result = task_service.update_task(sample_task)

    assert result.title == sample_task.title
    task_service.repository.update_task.assert_called_once()


def test_delete_task_success(task_service):
    task_service.repository.delete_task.return_value = None

    task_service.delete_task(1)

    task_service.repository.delete_task.assert_called_once_with(1)


def test_get_tasks_success(task_service, sample_task):
    task_service.repository.get_tasks.return_value = [sample_task]

    result = task_service.get_tasks()

    assert isinstance(result, list)
    assert result[0].title == sample_task.title
