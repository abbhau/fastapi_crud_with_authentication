from celery import Celery
from time import sleep
from celery.schedules import crontab

celery = Celery(__name__, broker="redis://127.0.0.1:6379/0", backend="redis://127.0.0.1:6379/0")


@celery.task
def add():
        return {"hi" : "bro"}


celery.conf.beat_schedule = {
    'run-every-minute': {
        'task': 'worker.add',
        'schedule': crontab(minute='*/1'),
    },
}
