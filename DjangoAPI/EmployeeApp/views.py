from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
#to other domain access our apis ie, frontend projects
from rest_framework.parsers import JSONParser
#to parse incoming data to data models
from django.http.response import JsonResponse
from django.core.files.storage import default_storage

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer
#Serializers allow complex data such as querysets and model instances to be 
# converted to native Python datatypes that can then be easily rendered into JSON , 
# XML or other content types.


# Create your views here.
@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse('Added successfully', safe=False)
        return JsonResponse('Failed to add', safe=False)
    elif request.method == 'PUT':
         department_data = JSONParser().parse(request)
         department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
         departments_serializer = DepartmentSerializer(department, data =department_data)
         if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse('updated successfully', safe=False)
         return JsonResponse('Failed to update', safe=False)
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId = id)
        department.delete()
        return JsonResponse('Deleted Successfully', safe=False)



@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer=EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)



