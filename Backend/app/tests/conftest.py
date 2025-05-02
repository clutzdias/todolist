import pytest
from app.models.task import Task
from app.task_service import TaskService
from app.database.task_repository import TaskRepository

@pytest.fixture
def sample_task():
    return Task(title="Test Task", description="A test task", completed=False)

@pytest.fixture
def mock_repository(mocker):
    return mocker.Mock(spec=TaskRepository)

@pytest.fixture
def task_service(mock_repository):
    service = TaskService()
    service.repository = mock_repository
    return service