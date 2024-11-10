
from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee
from django.shortcuts import get_object_or_404

# Create your views here.

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk) #Il primo pk specifica il campo della classe Employee, alias di id, il secondo pk è il nome del parametro stabilito nell'urls
    print(employee)
    context = {
        'employee': employee
    }
    #return HttpResponse(employee.designation)
    return render(request, 'employee_detail.html', context)