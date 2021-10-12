from api.backend.views import get_readme
from celery import shared_task

@shared_task
def call_get_readme():
    return get_readme(None, 'allan-testing-organization')
