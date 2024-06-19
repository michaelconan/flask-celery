"""
test_tasks.py

This module demonstrates how to use pytest to unit test Celery tasks with the Flask + Celery application factory pattern.
"""

import pytest
from src.task_app import create_app, tasks


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


def test_add_task(app):
    result = tasks.add(1, 2)
    assert result == 3
