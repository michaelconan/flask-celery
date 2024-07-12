"""
test_tasks.py

This module demonstrates how to use pytest to unit test Celery tasks with the Flask + Celery application factory pattern.
"""

import pytest
from src.task_app import tasks


def test_add_task(app):
    """ Unit test to validate the celery add task
    """
    # GIVEN
    number1 = 1
    number2 = 2

    # WHEN
    result = tasks.add(number1, number2)

    # THEN
    assert result == 3
