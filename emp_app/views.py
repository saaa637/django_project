from django.shortcuts import render, redirect
from .models import Person, Department, Role
from django.db.models import Q


def index(request):
    return render(request, 'index.html')


def view_emp(request):
    emps = Person.objects.all()
    return render(request, 'view_emp.html', {'emps': emps})


def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept_id = request.POST['dept']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        role_id = request.POST['role']

        new_emp = Person(
            first_name=first_name,
            last_name=last_name,
            dept_id=dept_id,
            salary=salary,
            bonus=bonus,
            role_id=role_id
        )
        new_emp.save()
        return redirect('home')

    depts = Department.objects.all()
    roles = Role.objects.all()
    return render(request, 'add_emp.html', {'depts': depts, 'roles': roles})


def remove_emp(request):
    emps = Person.objects.all()
    return render(request, 'remove_emp.html', {'emps': emps})


def filter_emp(request):
    if request.method=="POST":
        name = request.POST['name']
        dept = request.POST['dept']

        emps = Person.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name))

        if dept:
            emps = emps.filter(dept__name__icontains=dept)

        return render(request, 'view_emp.html', {'emps': emps})

    return render(request, 'filter_emp.html')
# def remove_emp_by_id(request, emp_id):
#     emp = Person.objects.get(id=emp_id)
#     emp.delete()
#     return redirect('view_emp')


from django.shortcuts import get_object_or_404


def remove_emp_by_id(request, emp_id):
    emp = get_object_or_404(Person, id=emp_id)
    emp.delete()
    return redirect('/')   # redirects to home page
