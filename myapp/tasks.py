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
    sleep(40)
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
 
@shared_task(name='update_job_name_only')
def update_job_name_only():
    # sleep(30)
    jobs=Job.objects.all()
    faker=Faker()
    
    for job in jobs:
        if(job.name!="Mission"):
            job.name="Mission"
        else:
            job.name=faker.name()
        job.save()   
        
 
@shared_task(name='update_job_pipeline_only')
def update_job_pipeline_only():
    # sleep(30)
    jobs=Job.objects.all()
    faker=Faker()
    
    for job in jobs:
        if(job.pipeline!="No Pipeline"):
            job.name="No Pipeline"
        else:
            job.pipeline=faker.word()
        job.save()   


@shared_task(name='update_job_cluster_only')
def update_job_cluster_only():
    # sleep(30)
    jobs=Job.objects.all()
    faker=Faker()
    
    for job in jobs:
        if(job.cluster!="No Cluster"):
            job.name="No Cluster"
        else:
            job.cluster=faker.name()
        job.save()   
        

#     PeriodicTask.objects.get_or_create(    name=f'cluster_update_task{i}',    task='update_job_cluster_only',    interval=first_interval,   one_off=False )
# for i in range(0, 10):
    
#     PeriodicTask.objects.get_or_create(    name=f'pipeline_update_task{i}',    task='update_job_pipeline_only',    interval=first_interval,   one_off=False )