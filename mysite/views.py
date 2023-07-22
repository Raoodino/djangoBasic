from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee

def home(request):
    #return HttpResponse('')
    #retrieve all the data from database
    employees = Employee.objects.all()
    print(employees)
    context = {
        'employees': employees,
    }
    return render(request, 'home.html', context)