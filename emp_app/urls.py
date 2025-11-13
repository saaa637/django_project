"""
URL configuration for office_emp_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from emp_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', views.index, name="home"),

    # View all employees
    path('view_emp', views.view_emp, name="view_emp"),

    # Add employee
    path('add_emp', views.add_emp, name="add_emp"),

    # Remove employee page (list)
    path('remove_emp', views.remove_emp, name="remove_emp"),

    # # Remove employee by ID
    # path('remove_emp/<int:emp_id>', views.remove_emp_by_id, name="remove_emp_by_id"),

    path('remove_emp/<int:emp_id>/delete/', views.remove_emp_by_id, name='remove_emp_by_id'),


    # Filter employee
    path('filter_emp', views.filter_emp, name="filter_emp"),
]

