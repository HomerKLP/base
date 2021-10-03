import os

from celery import Celery
from celery.result import AsyncResult
from kombu import Queue, Exchange

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


class MyCelery(Celery):
    def remote_call(
            self, task_name: str, routing_key: str, payload: dict,
            exchange: str, exchange_type: str = "direct",
    ) -> AsyncResult:
        exchange = Exchange(name=exchange, type=exchange_type)
        return self.send_task(
            name=task_name,
            routing_key=routing_key,
            kwargs=payload,
            exchange=exchange,
            declare=(exchange,),
        )


celery_app = MyCelery('core')
celery_app.config_from_object(
    obj='django.conf:settings', namespace='CELERY',
)
celery_app.autodiscover_tasks()

celery_app.conf.task_queues = (
    Queue(
        name="base.medium",
        routing_key="base.medium",
    ),
)
celery_app.conf.task_default_exchange = "base"
celery_app.conf.task_default_exchange_type = "direct"
