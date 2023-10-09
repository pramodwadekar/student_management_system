from django.shortcuts import render, redirect
from .models import student
from django.contrib import messages
from django.db.models import Q

def index(request):
    students = student.objects.all()
    query = ""

    if request.method == "POST":
        if "add" in request.POST:
            name = request.POST.get("name")
            dob = request.POST.get("dob")
            email = request.POST.get("email")
            contact = request.POST.get("contact")
            gender = request.POST.get("gender")
            country = request.POST.get("country")
            state = request.POST.get("state")
            city = request.POST.get("city")
            pincode = request.POST.get("pincode")
            qualification = request.POST.get("qualification")
            student.objects.create(Fullname = name, DOB = dob, Email = email, Contact = contact,
                                   Gender = gender, Country = country, State = state, City = city, 
                                   Pincode = pincode, Qualification = qualification)
            messages.success(request, "New Student Added Successfull")
            return redirect('index')
        
        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            dob = request.POST.get("dob")
            email = request.POST.get("email")
            contact = request.POST.get("contact")
            gender = request.POST.get("gender")
            country = request.POST.get("country")
            state = request.POST.get("state")
            city = request.POST.get("city")
            pincode = request.POST.get("pincode")
            qualification = request.POST.get("qualification")

            Update_student = student.objects.get(id=id)
            Update_student.Fullname = name
            Update_student.DOB = dob
            Update_student.Email = email
            Update_student.Contact = contact
            Update_student.Gender = gender
            Update_student.Country = country
            Update_student.State = state
            Update_student.City = city
            Update_student.Pincode = pincode
            Update_student.Qualification = qualification
            Update_student.save()

            messages.success(request, "Student Data Updated Successfull")
            return redirect('index')

        elif "delete" in request.POST:
            id = request.POST.get("id")
            student.objects.get(id=id).delete()  
            messages.success(request, "Student Deleted Successfully")
            return redirect('index')


        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            students = student.objects.filter(Q(Fullname__icontains=query) | Q(DOB__icontains=query) | Q(Email__icontains=query) |
                                              Q(Contact__icontains=query) | Q(Gender__icontains=query) | Q(City__icontains=query) | 
                                              Q(Qualification__icontains=query))

    context = {"students" : students, "query" : query}
    return render(request, 'index.html', context = context)

