from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Employee
import json

def get_name(request):
        if request.method == 'POST':
            received_json_data=json.loads(request.body.decode("utf-8"))
            print(received_json_data)
            email = received_json_data["email"]
            department = received_json_data["department"]
            phone = received_json_data["phone"]
            address = received_json_data["address"]
            password = received_json_data["password"]
            print(department)
            user = User.objects.create_user(email,email,password)
            
            user.save()
            
            e = Employee(user = User.objects.get(username=email),email=email,department=department,phone=phone,address=address)
            e.save()
            return HttpResponse('thanks')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = Employee()
    
        return HttpResponse(str(e))

def getEmployeeData(request):
    received_json_data=json.loads(request.body.decode("utf-8"))
    id = received_json_data["id"]
    print("id",id)
    e = Employee.objects.filter(email=id.strip()).values()
    return JsonResponse(list(e),safe=False)

def updateEmployeeData(request):
    received_json_data=json.loads(request.body.decode("utf-8"))
    id = received_json_data["id"]
    department = received_json_data["department"]
    phone = received_json_data["phone"]
    address = received_json_data["address"]
    
    print("id",id)
    print("department",department)
    print("phone",phone)
    print("address",address)

    
    e = Employee.objects.get(email=id.strip())
    e.department = department
    e.phone = int(phone)
    e.address = address
    e.save()
    return JsonResponse({"success"})