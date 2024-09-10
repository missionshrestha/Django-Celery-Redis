from celery import shared_task
from time import sleep
import json
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from faker import Faker

from myapp.models import Job

# @shared_task(name='subtraction_task')
# def sub(x, y):
#     sleep(5)
#     return x - y

# @shared_task
# def clear_session_cache(id):
#     print(f"Session Cache Cleared : {id}")
#     return id

# @shared_task
# def clear_redis_data(key):
#     print(f"Redis Data Cleared : {key}")
#     return key

# @shared_task
# def clear_rabbitmq_data(key):
#     print(f"RabbitMQ Data Cleared : {key}")
#     return key


# Create Schedule every 20 seconds
# schedule, created = IntervalSchedule.objects.get_or_create(
#     every=20, 
#     period=IntervalSchedule.SECONDS,
#     )

# # Schedule the periodic task programmatically
# PeriodicTask.objects.get_or_create(
#     name='Clear RabbitMQ Periodic Task',
#     task='myapp.tasks.clear_rabbitmq_data',
#     interval=schedule,
#     args=json.dumps(['hello rabbitMQ']),
# )




@shared_task(name='update_jobssssss')
def update_job():
    sleep(5)
    jobs=Job.objects.all()
    faker=Faker()
    
    for job in jobs:
        job.name=faker.name()
        job.pipeline=faker.word()
        job.cluster=faker.name()
        job.enabled=faker.boolean()
        job.schedule=faker.date_time_this_year()
        job.description=faker.text()
        job.save()
    