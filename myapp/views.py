from django.shortcuts import render
from myceleryproject.celery import add
from myapp.tasks import sub
# Create your views here.

# # Enqueue the task using delay method
# def index(request):
#     print("Results: ")
#     result2=add.delay(10,20)
#     print("Result2: ",result2)
#     result3=sub.delay(5,4)
#     print("Result3: ",result3)
#     # result1=add(10,20)f
#     # print("Results: ",result1)
    
#     return render(request, 'myapp/home.html')

# Enqueue the task using async method
def index(request):
    print("Results: ")
    result2=add.apply_async(([10,20]))
    print("Result2: ",result2)
    result3=sub.apply_async(([10,20]))
    print("Result3: ",result3)
    # result1=add(10,20)f
    # print("Results: ",result1)
    
    return render(request, 'myapp/home.html')

def about(request):
    print("Results: ")
    return render(request, 'myapp/about.html')

def contact(request):
    print("Results: ")
    return render(request, 'myapp/contact.html')