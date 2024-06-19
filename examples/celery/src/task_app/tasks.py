import time

from celery import shared_task
from celery import Task
from flask import current_app


@shared_task(ignore_result=False)
def add(a: int, b: int) -> int:
    print(f'Running app: {current_app.name}, debug: {
          current_app.config["DEBUG"]}')
    return a + b


@shared_task()
def block() -> None:
    time.sleep(5)


@shared_task(bind=True, ignore_result=False)
def process(self: Task, total: int) -> object:
    for i in range(total):
        self.update_state(state="PROGRESS", meta={
                          "current": i + 1, "total": total})
        time.sleep(1)

    return {"current": total, "total": total}
