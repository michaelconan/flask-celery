"""
test_views.py

This module demonstrates how to use pytest to unit test Flask views with the Flask application factory pattern.
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


@pytest.fixture()
def client(app):
    return app.test_client()


def test_request_example(client):
    response = client.get("/")
    assert b"<h2>Celery Example</h2>" in response.data
