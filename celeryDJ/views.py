from django.http import HttpResponse
from .tasks import your_async_task
from django.http import JsonResponse
# def my_view(request):
#     # Your logic here
#     return HttpResponse("Hello, this is my first view!")

def my_view(request):
    # Call the asynchronous task using delay() method
    task_result = your_async_task.delay(10, 20)
    return JsonResponse({'task_id': task_result.id})

