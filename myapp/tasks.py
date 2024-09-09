from celery import shared_task
from time import sleep
import json

@shared_task(name='subtraction_task')
def sub(x, y):
    sleep(5)
    return x - y

@shared_task
def clear_session_cache(id):
    print(f"Session Cache Cleared : {id}")
    return id

@shared_task
def clear_redis_data(key):
    print(f"Redis Data Cleared : {key}")
    return key

@shared_task
def clear_rabbitmq_data(key):
    print(f"RabbitMQ Data Cleared : {key}")
    return key

from django_celery_beat.models import PeriodicTask, IntervalSchedule

# Create Schedule every 20 seconds
schedule, created = IntervalSchedule.objects.get_or_create(
    every=20, 
    period=IntervalSchedule.SECONDS,
    )

# Schedule the periodic task programmatically
PeriodicTask.objects.get_or_create(
    name='Clear RabbitMQ Periodic Task',
    task='myapp.tasks.clear_rabbitmq_data',
    interval=schedule,
    args=json.dumps(['hello rabbitMQ']),
)