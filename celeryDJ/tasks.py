from celery import shared_task
from celeryDJ.celery import app

@shared_task
def your_async_task(arg1, arg2):
    # Your asynchronous task logic here
    result = arg1 + arg2
    return result

@app.task
def your_periodic_task():
    # Your periodic task logic here
    # This task will run at the specified interval
    print("This is a periodic task.")