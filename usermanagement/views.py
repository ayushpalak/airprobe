from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Employee
import json

def get_name(request):
    try:
        user = None
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
            
            return JsonResponse({"result":"success"},safe=False)

        # if a GET (or any other method) we'll create a blank form
        else:
            return JsonResponse({"error":"Not a post request."},safe=False)
    except Exception as e:
        User.objects.get(username=email).delete()
        return JsonResponse({"error":str(e)},safe=False)

def getEmployeeData(request):
    try:
        received_json_data=json.loads(request.body.decode("utf-8"))
        id = received_json_data["id"]
        print("id",id)
        e = Employee.objects.filter(email=id.strip()).values()
        return JsonResponse(list(e),safe=False)
    except Exception as e:
        return JsonResponse({"error":str(e)},safe=False)

def updateEmployeeData(request):
    try:
        received_json_data=json.loads(request.body.decode("utf-8"))
        id = received_json_data["id"]
        department = received_json_data["department"]
        phone = received_json_data["phone"]
        address = received_json_data["address"]
        
        e = Employee.objects.get(email=id.strip())
        e.department = department
        e.phone = int(phone)
        e.address = address
        e.save()
        return JsonResponse({"result":"success"},safe=False)
    except Exception as e:
        return JsonResponse({"error":str(e)},safe=False)
def  register(request):
    return render(request,'register.html')

def delete_account(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
        print("user",user.username)
        User.objects.get(username=user.username).delete()
        return HttpResponse("User Deleted Successfully.")
    return HttpResponse("no user logged in.")