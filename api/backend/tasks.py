from os import name
from celery import shared_task
from api.celery import app
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from api.backend.views import get_readme
# from ..celery import app


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Executes every Monday morning at 7:30 a.m.
#     # sender.add_periodic_task(
#     #     crontab(hour=8, m/inute=00, day_of_week=1),
#     #     call_get_readme(),
#     # )

#      # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, call_get_readme(), expires=10)


logger = get_task_logger(__name__)

@app.task(name='call_get_readme')
def call_get_readme():
    logger.info("get_readme iniciou!")
    return get_readme(None, 'allan-testing-organization')
