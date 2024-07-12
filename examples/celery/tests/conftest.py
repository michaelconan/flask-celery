import pytest
from src.task_app import create_app


@pytest.fixture()
def app():
    """ Fixture to create flask app from factory
    and initiate app context
    """
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    with app.app_context():
        yield app


@pytest.fixture()
def client(app):
    """ Fixture to create test client for view tests
    """
    return app.test_client()