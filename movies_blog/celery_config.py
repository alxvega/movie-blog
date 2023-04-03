from celery import Celery
from celery_task import BaseScraperTask
from django.conf import settings

app = Celery("scraper", task_cls=BaseScraperTask)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    broker_transport_options={"visibility_timeout": 18000},
    task_reject_on_worker_lost=True,
)

app.conf.update(broker_pool_limit=settings.CELERY_BROKER_POOL_LIMIT)

app.autodiscover_tasks()
